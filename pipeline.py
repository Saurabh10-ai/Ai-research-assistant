
from agent import build_read_agent , build_search_agent , writer_chain , critic_chain
from langchain_community.callbacks import get_openai_callback
from langchain_core.callbacks import BaseCallbackHandler

class SimpleTokenCounter(BaseCallbackHandler):

  def __init__(self):
    self.total_tokens = 0
    self.prompt_tokens = 0
    self.completion_tokens = 0

  def on_llm_end(self, response, **kwargs):

    usage = None

    # Method 1: OpenAI-style token usage
    if response.llm_output:
      usage = response.llm_output.get("token_usage")

    # Method 2: LangChain usage metadata
    if not usage:
      for generation_list in response.generations:
        for generation in generation_list:

          message = getattr(generation, "message", None)

          if message:
            usage = getattr(message, "usage_metadata", None)

            if not usage:
              metadata = getattr(message, "response_metadata", {})
              usage = metadata.get("token_usage")

          if usage:
            break

        if usage:
          break

    if not usage:
      print("Warning: Token usage metadata not found")
      return

    prompt = usage.get("prompt_tokens", usage.get("input_tokens", 0))
    completion = usage.get("completion_tokens", usage.get("output_tokens", 0))
    total = usage.get("total_tokens", prompt + completion)

    self.prompt_tokens += prompt
    self.completion_tokens += completion
    self.total_tokens += total

    print(f"\nToken Usage: Prompt={prompt}, Completion={completion}, Total={total}")


# makeing pipline

def run_research_pipeline(topic : str) -> dict:

    token_tracker = SimpleTokenCounter()
    state = {}

    # Initialize callback configuration
    config = {"callbacks": [token_tracker]}

    # Wrap the entire pipeline in the callback context manager

    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke(
        {
            "messages": [
                ("user", f"Find recent, reliable and detailed information about: {topic}")
            ]
        },
             config=config
        )

    state["search_results"] = search_result['messages'][-1].content

    print("\n search result ",state['search_results'])

        #step 2 - reader agent
    print("\n"+" ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    reader_agent = build_read_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    }, config=config)

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nscraped content: \n", state['scraped_content'])

   #step 3 - writer chain

    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    }, config=config)

    print("\n Final Report\n",state['report'])
        #critic report

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report":state['report']
    }, config=config)

    print("\n critic report \n", state['feedback'])

    # Total token usage from all agents and chains
    state["token_usage"] = {
        "total_tokens": token_tracker.total_tokens,
        "prompt_tokens": token_tracker.prompt_tokens,
        "completion_tokens": token_tracker.completion_tokens
    }

    print("\n" + "="*50)
    print("TOTAL TOKEN USAGE")
    print("="*50)
    print("Prompt Tokens:", token_tracker.prompt_tokens)
    print("Completion Tokens:", token_tracker.completion_tokens)
    print("Total Tokens:", token_tracker.total_tokens)

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
