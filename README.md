# 🛒 Customer Review Sentiment Analyzer (NLP Project)

## 📖 Overview

This project is a Natural Language Processing (NLP) web application that analyzes Amazon product reviews to predict sentiment — **Positive 😊** or **Negative 😞**.
It demonstrates the complete ML lifecycle: data preprocessing, feature extraction, model training, evaluation, and deployment.

## 🎯 Objective

E-commerce companies receive millions of reviews daily.
Manually identifying customer sentiment is time-consuming.
This project automates that process using **TF-IDF + Logistic Regression**, helping businesses understand customer opinions quickly.

## ⚙️ Workflow

### 1️⃣ Data Source

* Dataset: Amazon Reviews (FastText format)
* Labels:

  * `__label__1` = Positive
  * `__label__2` = Negative

### 2️⃣ Data Preprocessing

* Lowercasing
* Removing punctuation and digits
* Stripping extra spaces
* Tokenization

### 3️⃣ Feature Engineering

* TF-IDF Vectorizer (**10,000 max features**)
* Converts text into numerical vectors

### 4️⃣ Model Building

Trained and compared:

* **Logistic Regression → ~92% accuracy**
* **XGBoost → ~90% accuracy**

### 5️⃣ Deployment

* Interactive Streamlit web app
* Real-time sentiment prediction
* Deployed on **Hugging Face Spaces**

## 💻 Tech Stack

* Python
* Streamlit
* scikit-learn
* xgboost
* pandas, numpy
* joblib
* Hugging Face Spaces

## 🧠 How It Works

1. User inputs a product review
2. Text is preprocessed
3. Converted using saved TF-IDF vectorizer
4. Trained LR model predicts sentiment
5. Displays: **😊 Positive** or **😞 Negative**

## 🚀 Live Demo

🔗 Hugging Face App: [https://huggingface.co/spaces/manishadharmik/customer-review-sentiment-analyzer](https://huggingface.co/spaces/manishadharmik/customer-review-sentiment-analyzer)
📦 GitHub Repo: [https://github.com/manishadharmik7/amazon-sentiment.git](https://github.com/manishadharmik7/amazon-sentiment.git)

## 📂 Folder Structure

```
amazon-sentiment/
│── app.py                     # Streamlit application
│── sentiment_lr_model.pkl     # Logistic Regression model
│── tfidf_vectorizer.pkl       # TF-IDF vectorizer
│── requirements.txt           # Dependencies
│── README.md                  # Documentation
└── data/                      # (optional) dataset for testing
```

## 📊 Results

| Model               | Accuracy | Features |
| ------------------- | -------- | -------- |
| Logistic Regression | 92%      | TF-IDF   |
| XGBoost             | 90%      | TF-IDF   |

## 🏆 Skills Demonstrated

* Natural Language Processing
* Text Preprocessing
* TF-IDF Vectorization
* Logistic Regression, XGBoost
* Streamlit App Development
* Model Deployment (Hugging Face)

---

