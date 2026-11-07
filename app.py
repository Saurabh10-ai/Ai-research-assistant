
import streamlit as st
from datetime import datetime

from pipeline import run_research_pipeline


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Research Analyst",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

.stApp {
    background: linear-gradient(135deg, #080d1b 0%, #111a32 55%, #15112b 100%);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main heading */

.main-title {
    font-size: 43px;
    font-weight: 900;
    letter-spacing: -1.5px;
    background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #a5b4fc;
    font-size: 15px;
    margin-top: 8px;
}

/* Headings */

h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 800 !important;
}

/* General text */

p, label, li {
    color: #e2e8f0;
    line-height: 1.7;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #172554);
    border-right: 1px solid #334155;
}

section[data-testid="stSidebar"] * {
    color: #e0f2fe;
}

/* Text area */

.stTextArea textarea {
    background: #17243b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    border-radius: 14px !important;
    font-size: 16px !important;
    padding: 15px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #22d3ee !important;
    box-shadow: 0 0 12px #22d3ee33 !important;
}

/* Buttons */

.stButton button {
    background: linear-gradient(90deg, #0891b2, #6366f1);
    color: white !important;
    border: none;
    border-radius: 11px;
    padding: 11px 18px;
    font-size: 14px;
    font-weight: 700;
    transition: 0.3s;
}

.stButton button:hover {
    background: linear-gradient(90deg, #06b6d4, #8b5cf6);
    box-shadow: 0 0 20px #6366f155;
    transform: translateY(-2px);
}

/* Metric cards */

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #172554, #312e81);
    padding: 20px;
    border: 1px solid #6366f1;
    border-radius: 15px;
}

[data-testid="stMetricLabel"] {
    color: #bae6fd !important;
    font-size: 14px !important;
}

[data-testid="stMetricValue"] {
    color: #67e8f9 !important;
    font-size: 29px !important;
    font-weight: 800 !important;
}

/* Tabs */

.stTabs [data-baseweb="tab"] {
    color: #cbd5e1;
    font-weight: 700;
    font-size: 14px;
}

.stTabs [aria-selected="true"] {
    color: #22d3ee !important;
    border-bottom: 3px solid #22d3ee !important;
}

/* Download button */

.stDownloadButton button {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white !important;
    border-radius: 10px;
    font-weight: 700;
}

/* Expanders */

div[data-testid="stExpander"] {
    background: #17243b;
    border: 1px solid #334155;
    border-radius: 12px;
}

/* Alerts */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Divider */

hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================

if "research_data" not in st.session_state:
    st.session_state.research_data = None

if "research_history" not in st.session_state:
    st.session_state.research_history = []


# =====================================================
# HELPER FUNCTION
# =====================================================

def get_content(value):

    if value is None:
        return "No content available."

    if isinstance(value, str):
        return value

    if hasattr(value, "content"):
        content = value.content

        if isinstance(content, str):
            return content

        return str(content)

    return str(value)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## 🔬 Research Analyst")

    st.caption("Multi-Agent AI Research System")

    st.divider()

    st.markdown("### ⚙️ System Architecture")

    st.markdown("""
    🔎 **Search Agent**

    Finds relevant research sources.

    ---

    📚 **Reader Agent**

    Extracts detailed information.

    ---

    ✍️ **Writer Chain**

    Generates research reports.

    ---

    🧠 **Critic Chain**

    Evaluates report quality.
    """)

    st.divider()

    st.markdown("### 🛠️ Technologies")

    st.markdown("""
    - Python
    - LangChain
    - Streamlit
    - LLM APIs
    - BeautifulSoup
    """)

    st.divider()

    st.caption("AI Research Analyst | 2026")


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">✦ AI Research Analyst</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover • Analyze • Research • Generate • Evaluate'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# =====================================================
# RESEARCH INPUT
# =====================================================

st.markdown("## ✨ Start Your Research")

st.markdown(
    "Enter a research topic and let your AI agents investigate it."
)

topic = st.text_area(
    "Research Topic",
    placeholder=(
        "Example: Impact of Generative AI on employment "
        "between 2026 and 2030..."
    ),
    height=120,
    key="research_topic"
)


col1, col2 = st.columns([1, 1])

with col1:

    start_button = st.button(
        "🚀 Start Research",
        type="primary",
        use_container_width=True
    )

with col2:

    clear_button = st.button(
        "🗑️ Clear Results",
        use_container_width=True
    )


# =====================================================
# CLEAR RESULTS
# =====================================================

if clear_button:

    st.session_state.research_data = None

    st.rerun()


# =====================================================
# RUN RESEARCH PIPELINE
# =====================================================

if start_button:

    if not topic.strip():

        st.warning("Please enter a research topic first.")

    else:

        try:

            with st.status(
                "🔬 AI Research Analyst is working...",
                expanded=True
            ) as status:

                st.write("🔎 Step 1: Search Agent is finding sources.")

                st.write("📚 Step 2: Reader Agent is extracting content.")

                st.write("✍️ Step 3: Writer Chain is preparing the report.")

                st.write("🧠 Step 4: Critic Chain is reviewing the report.")

                # Execute your existing pipeline
                result = run_research_pipeline(topic.strip())

                # Save results
                st.session_state.research_data = result

                # Save history
                st.session_state.research_history.insert(
                    0,
                    {
                        "topic": topic.strip(),
                        "date": datetime.now().strftime(
                            "%d %b %Y, %I:%M %p"
                        )
                    }
                )

                status.update(
                    label="✅ Research completed successfully!",
                    state="complete",
                    expanded=False
                )

            st.success("Your research report is ready!")

        except Exception as e:

            st.error(f"Research pipeline failed: {str(e)}")


# =====================================================
# DISPLAY RESEARCH RESULTS
# =====================================================

data = st.session_state.research_data

if data:

    st.divider()

    st.markdown("## 📊 Research Analytics")

    # Get token information
    usage = data.get("token_usage", {})

    total_tokens = usage.get("total_tokens", 0)

    prompt_tokens = usage.get("prompt_tokens", 0)

    completion_tokens = usage.get("completion_tokens", 0)

    # Token metrics
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="🔵 Total Tokens",
            value=f"{total_tokens:,}"
        )

    with col2:

        st.metric(
            label="🟣 Prompt Tokens",
            value=f"{prompt_tokens:,}"
        )

    with col3:

        st.metric(
            label="🟢 Completion Tokens",
            value=f"{completion_tokens:,}"
        )

    st.write("")

    st.divider()

    # Get research content
    report = get_content(data.get("report"))

    search_results = get_content(data.get("search_results"))

    scraped_content = get_content(data.get("scraped_content"))

    feedback = get_content(data.get("feedback"))

    # =================================================
    # RESULT TABS
    # =================================================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Final Report",
        "🔎 Search Results",
        "📚 Scraped Content",
        "🧠 Critic Feedback"
    ])

    # FINAL REPORT

    with tab1:

        st.markdown("### 📄 Final Research Report")

        st.markdown(report)

        st.divider()

        st.download_button(
            label="⬇️ Download Research Report",
            data=report,
            file_name="AI_Research_Report.md",
            mime="text/markdown",
            use_container_width=True
        )

    # SEARCH RESULTS

    with tab2:

        st.markdown("### 🔎 Search Agent Results")

        st.markdown(search_results)

        st.download_button(
            label="⬇️ Download Search Results",
            data=search_results,
            file_name="search_results.txt",
            mime="text/plain"
        )

    # SCRAPED CONTENT

    with tab3:

        st.markdown("### 📚 Extracted Research Content")

        st.markdown(scraped_content)

        st.download_button(
            label="⬇️ Download Scraped Content",
            data=scraped_content,
            file_name="scraped_content.txt",
            mime="text/plain"
        )

    # CRITIC FEEDBACK

    with tab4:

        st.markdown("### 🧠 Critic Agent Review")

        st.markdown(feedback)

        st.download_button(
            label="⬇️ Download Critic Feedback",
            data=feedback,
            file_name="critic_feedback.txt",
            mime="text/plain"
        )


# =====================================================
# EMPTY STATE
# =====================================================

else:

    st.divider()

    st.markdown("## 👋 Welcome to your Research Workspace")

    st.info(
        "Enter a research topic above and click Start Research "
        "to generate your first AI-powered research report."
    )

    st.markdown("### Your Research Workflow")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### 🔎")
        st.markdown("**Search**")
        st.caption("Discover reliable sources.")

    with col2:
        st.markdown("### 📚")
        st.markdown("**Read**")
        st.caption("Extract detailed information.")

    with col3:
        st.markdown("### ✍️")
        st.markdown("**Write**")
        st.caption("Generate a structured report.")

    with col4:
        st.markdown("### 🧠")
        st.markdown("**Critic**")
        st.caption("Review and improve the report.")


# =====================================================
# RESEARCH HISTORY
# =====================================================

st.divider()

with st.expander("🕒 Research History", expanded=False):

    if st.session_state.research_history:

        for item in st.session_state.research_history:

            st.markdown(f"**🔬 {item['topic']}**")

            st.caption(item["date"])

            st.divider()

    else:

        st.caption("No research history available yet.")
