# Machine Learning

## Introduction

Machine learning (ML) is a branch of artificial intelligence (AI) that enables computers to learn patterns from data and use those patterns to make predictions, decisions, or recommendations. Instead of programming every rule explicitly, we provide an algorithm with examples and allow it to improve its performance through experience.

For example, an email service can learn from previously labelled messages to identify whether a new message is likely to be spam. A recommendation system can learn from a user's past activity to suggest films, products, or music.

## How Machine Learning Works

Most machine-learning systems follow these steps:

1. **Define the problem** – Decide what should be predicted or automated.
2. **Collect data** – Gather relevant and representative examples.
3. **Prepare the data** – Clean errors, handle missing values, and convert information into a suitable format.
4. **Select a model** – Choose an algorithm appropriate for the problem and the available data.
5. **Train the model** – Give the model training examples so that it can learn relationships in the data.
6. **Evaluate the model** – Test its performance on data that it has not seen during training.
7. **Deploy and monitor** – Use the model in a real application and check that its performance remains reliable.

A common division of a dataset is:

- **Training set:** Used to learn model parameters.
- **Validation set:** Used to compare models and tune settings.
- **Test set:** Used only for the final, unbiased evaluation.

## Main Types of Machine Learning

### 1. Supervised Learning

In supervised learning, the algorithm learns from labelled data. Each example includes both the input and the correct output.

- **Classification** predicts a category, such as spam or not spam.
- **Regression** predicts a numerical value, such as house price or temperature.

Common supervised-learning algorithms include linear regression, logistic regression, decision trees, random forests, support vector machines, and neural networks.

### 2. Unsupervised Learning

Unsupervised learning uses data without labelled answers. The algorithm attempts to discover structure or relationships in the data.

- **Clustering** groups similar examples, such as customers with similar purchasing behaviour.
- **Dimensionality reduction** represents data using fewer features while preserving important information.
- **Association analysis** discovers relationships, such as products that are frequently purchased together.

Examples of algorithms include k-means clustering, hierarchical clustering, principal component analysis (PCA), and autoencoders.

### 3. Semi-Supervised Learning

Semi-supervised learning combines a small amount of labelled data with a larger amount of unlabelled data. It is useful when labelling examples is expensive or requires expert knowledge, such as in medical imaging.

### 4. Reinforcement Learning

In reinforcement learning, an agent interacts with an environment. It takes actions, receives rewards or penalties, and learns a strategy that aims to maximize its total reward over time. This approach is used in robotics, game-playing systems, and some resource-management problems.

## Important Machine-Learning Concepts

### Features and Labels

A **feature** is an input property used by a model, such as age, income, or image pixels. A **label** is the desired output in a supervised-learning problem, such as a class name or a numerical target.

### Model and Parameters

A **model** is the mathematical representation used to make predictions. During training, the model learns **parameters** from data. Developers can also choose **hyperparameters**, such as a tree's maximum depth or a neural network's learning rate.

### Overfitting and Underfitting

- **Overfitting** occurs when a model memorizes the training data, including noise, and performs poorly on new examples.
- **Underfitting** occurs when a model is too simple to learn the important patterns in the data.

The goal is to find a model that generalizes well to unseen data. Techniques such as cross-validation, regularization, early stopping, data augmentation, and appropriate model complexity can help.

### Bias and Variance

**Bias** is error caused by overly simple assumptions. **Variance** is error caused by excessive sensitivity to the training data. The bias-variance trade-off describes the need to balance these two sources of error.

### Data Leakage

Data leakage happens when information that would not be available at prediction time is accidentally used during training. It can produce impressive test results that do not reflect real-world performance. Data preparation and feature engineering should therefore be performed carefully, especially when splitting data into training and test sets.

## Model Evaluation

The correct evaluation measure depends on the task.

### Classification Metrics

- **Accuracy:** The proportion of all predictions that are correct.
- **Precision:** Of the examples predicted as positive, the proportion that is actually positive.
- **Recall:** Of all actual positive examples, the proportion identified by the model.
- **F1-score:** The harmonic mean of precision and recall.
- **Confusion matrix:** A table showing true positives, true negatives, false positives, and false negatives.

Accuracy alone can be misleading when classes are imbalanced. For example, a system that labels every transaction as legitimate may appear accurate if fraud is rare, while detecting no fraud at all.

### Regression Metrics

- **Mean absolute error (MAE):** The average absolute difference between predictions and actual values.
- **Mean squared error (MSE):** The average squared difference between predictions and actual values.
- **Root mean squared error (RMSE):** The square root of MSE, expressed in the target's units.
- **R-squared:** A measure of how much variation in the target is explained by the model.

## Neural Networks and Deep Learning

A neural network consists of connected layers of artificial neurons. Each connection has a weight, and training adjusts these weights to reduce prediction error. **Deep learning** refers to neural networks with multiple layers that can learn increasingly complex representations.

Deep-learning models are especially effective for images, audio, natural language, and other high-dimensional data. Examples include:

- **Convolutional neural networks (CNNs)** for image and visual tasks.
- **Recurrent neural networks (RNNs)** for sequential data.
- **Transformers** for language, vision, and other sequence-based tasks.

Deep learning often requires substantial data and computational resources, but transfer learning can reduce the amount of task-specific training needed.

## Applications

Machine learning is used in many fields, including:

- Healthcare: disease-risk prediction and medical-image analysis.
- Finance: fraud detection, credit assessment, and market analysis.
- Education: personalized learning and performance prediction.
- Transportation: route optimization and autonomous-driving systems.
- Agriculture: crop monitoring and yield prediction.
- Cybersecurity: anomaly and intrusion detection.
- Business: recommendations, demand forecasting, and customer analysis.
- Natural-language processing: translation, search, summarization, and conversational assistants.

## Advantages

- It can process large amounts of data quickly.
- It can identify patterns that are difficult to describe with fixed rules.
- It can automate repetitive decisions and predictions.
- It can improve as new, high-quality data becomes available.
- It can provide personalized services and recommendations.

## Limitations and Ethical Concerns

Machine learning is not automatically objective or correct. Its quality depends heavily on the data, assumptions, and objectives used to build it.

- **Bias:** Historical or unrepresentative data can lead to unfair outcomes.
- **Privacy:** Training data may contain sensitive personal information.
- **Explainability:** Complex models can be difficult to interpret.
- **Security:** Models can be attacked or misled by carefully designed inputs.
- **Reliability:** Performance may decrease when real-world data changes.
- **Accountability:** Organizations must decide who is responsible for automated decisions.
- **Environmental cost:** Training and operating large models can consume significant energy.

Responsible development includes collecting data lawfully, measuring performance across relevant groups, protecting personal information, documenting limitations, keeping humans involved in high-impact decisions, and monitoring deployed systems.

## Best Practices

1. Start with a clear objective and a simple baseline model.
2. Use data that is relevant, representative, and of sufficient quality.
3. Keep training, validation, and test data separate.
4. Choose evaluation metrics that match the real cost of errors.
5. Check for bias, leakage, and imbalance before training.
6. Prefer the simplest model that meets the required performance.
7. Document the data, assumptions, model version, and limitations.
8. Monitor the model after deployment and retrain when the data or problem changes.

## Conclusion

Machine learning allows computers to learn from data and support predictions, classification, and decision-making. Its major approaches are supervised, unsupervised, semi-supervised, and reinforcement learning. Successful machine-learning projects require more than selecting an algorithm: they depend on a well-defined problem, good data, suitable evaluation, responsible deployment, and continuous monitoring. Used carefully, machine learning can improve efficiency and help solve complex problems, but its predictions should always be interpreted in the context of its data and limitations.
