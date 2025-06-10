# Twitter Named Entity Recognition (NER) Project
 A deep learning-based Named Entity Recognition system to extract key entities from tweets without relying on hashtags.
 
Twitter is a microblogging and social networking service where users post and interact with short messages known as **tweets**. With an average of over **500 million tweets per day**, Twitter hosts a massive amount of real-time, user-generated content that reflects trending topics, public sentiment, events, and opinions.

However, relying solely on **user-generated hashtags** to understand and categorize content is not effective — users often omit hashtags, misspell them, or use irrelevant ones. To address this challenge, we aim to build an **automated Named Entity Recognition (NER)** system that can extract important entities from tweets directly, independent of hashtags.

---

## 🚀 Project Objective

The objective of this project is to **train machine learning and deep learning models** to perform **Named Entity Recognition (NER)** on Twitter data. The goal is to automatically identify and classify entities such as:

- Persons (e.g., Elon Musk)
- Organizations (e.g., NASA, Google)
- Locations (e.g., New York, India)
- Events (e.g., Olympics)
- Miscellaneous (e.g., products, hashtags, etc.)

This system will help Twitter:
- Understand trends in real time
- Improve content categorization
- Enhance user recommendation and analytics

---


---

## 🧠 Approach

We experiment with multiple approaches for NER:

### 1. Rule-based and Statistical Models:
- Conditional Random Fields (CRF)
- Hidden Markov Models (HMM)

### 2. Deep Learning Models:
- BiLSTM with CRF
- BiLSTM with Attention

### 3. Transformer-based Models:
- **BERT** (Bidirectional Encoder Representations from Transformers)
  - Fine-tuned specifically for NER task on Twitter data

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, NumPy** for data handling
- **Scikit-learn** for baseline models
- **TensorFlow / PyTorch** for deep learning
- **HuggingFace Transformers** for BERT
- **Seqeval / sklearn.metrics** for evaluation
- **Matplotlib / Seaborn** for visualization
- **Jupyter Notebooks** for prototyping

---

## 📊 Evaluation Metrics

NER is evaluated using:

- **Precision**
- **Recall**
- **F1 Score**

Measured at entity level using the **BIO tagging format** (Beginning, Inside, Outside).

---




