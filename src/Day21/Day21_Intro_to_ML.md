# Day21 — Introduction to Machine Learning

**Definition**
Machine Learning (ML) is a method of creating systems that learn patterns from data instead of relying on fixed, manually written rules. 

In traditional programming, developers provide both the data and the instructions (rules) to produce the correct output. In contrast, Machine Learning systems are trained using data along with the correct answers, allowing the model to automatically discover the rules and make predictions on new, unseen data.

There are three main types of Machine Learning. 

**Supervised Learning** uses labeled data, meaning the correct output is already known (for example, spam email detection or predicting house prices from historical data). 

**Unsupervised Learning** works with unlabeled data and identifies hidden patterns or groupings on its own (such as customer segmentation based on purchasing behavior). 

**Reinforcement Learning** involves an agent that learns by interacting with an environment and receiving rewards or penalties for its actions (for example, game-playing AI or self-driving car decision systems).

# Types of Machine Learning

## Supervised Learning
Supervised Learning is a type of Machine Learning where the model is trained on labeled data, meaning each input example is paired with the correct output (answer). The goal is to learn a mapping from inputs to outputs so the model can predict the correct result for new, unseen data. It is commonly used for classification and regression problems.

## Unsupervised Learning
Unsupervised Learning uses unlabeled data, where no correct answers are provided. The model tries to discover hidden patterns, structures, or groupings within the data on its own. It is mainly used for clustering, association, and dimensionality reduction tasks.

## Reinforcement Learning
Reinforcement Learning involves an agent that learns by interacting with an environment. Instead of labeled examples, the agent receives rewards for good actions and penalties for bad ones. Over time, it learns a strategy (policy) that maximizes long-term rewards. This approach is commonly used in decision-making and control problems.

---

## Comparison Table: Real-World Examples

| Machine Learning Type | Key Idea                          | Real-World Example 1        | Real-World Example 2              |
|------------------------|-----------------------------------|-----------------------------|-----------------------------------|
| Supervised Learning    | Learn from labeled data           | Spam Email Detection        | House Price Prediction            |
| Unsupervised Learning  | Find hidden patterns in data      | Customer Segmentation       | Market Basket Analysis            |
| Reinforcement Learning | Learn via rewards and penalties   | Game-Playing AI             | Self-Driving Car Navigation       |

---

## Why This Matters
Choosing the correct learning type is critical because each approach solves different kinds of problems. Using the wrong framework means the model will not learn meaningful patterns, leading to poor or unusable results even if the implementation is technically correct.