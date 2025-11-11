# 🛒 Customer Review Sentiment Analyzer (NLP Project)

## 📖 Overview
This project is a **Natural Language Processing (NLP)** web application that analyzes **Amazon product reviews** to predict sentiment — **Positive 😊** or **Negative 😞**.  
It demonstrates the complete **ML lifecycle** — data preprocessing, feature extraction, model training, evaluation, and deployment.

---

## 🎯 Objective
E-commerce companies receive millions of reviews daily.  
Manually identifying customer sentiment is time-consuming.  
This project automates that process using **TF-IDF + Logistic Regression**, helping businesses understand customer opinions quickly.

---

## ⚙️ Workflow

### 1️⃣ Data Source
- Dataset: [Amazon Reviews (FastText)](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)
- Format: Pre-labeled text reviews (`__label__1` = Positive, `__label__2` = Negative)

### 2️⃣ Data Preprocessing
- Lowercasing  
- Removing punctuation and digits  
- Stripping extra spaces  
- Tokenization  

### 3️⃣ Feature Engineering
- Used **TF-IDF Vectorizer** (10,000 max features) to convert text into numerical vectors.

### 4️⃣ Model Building
Trained and compared:
- **Logistic Regression** → Accuracy ~92%  
- **XGBoost** → Accuracy ~90%

### 5️⃣ Deployment
- Built an **interactive Streamlit web app** for real-time sentiment prediction.
- Deployed successfully on **Hugging Face Spaces**.

---

## 💻 Tech Stack
- **Python**
- **Streamlit**
- **scikit-learn**
- **xgboost**
- **pandas**, **numpy**
- **joblib**
- **Hugging Face Spaces**

---

## 🧠 How It Works
1. User inputs a product review.
2. Text is preprocessed and converted using the saved TF-IDF vectorizer.
3. The trained Logistic Regression model predicts sentiment.
4. The app displays “😊 Positive” or “😞 Negative” instantly.

---

## 🚀 Live Demo
🔗 **[Try the App Here (Hugging Face)](https://huggingface.co/spaces/manishadharmik/customer-review-sentiment-analyzer)**

---

## 📂 Folder Structure
amazon-sentiment/
│
├── app.py # Streamlit application
├── sentiment_lr_model.pkl # Trained Logistic Regression model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── data/ # (optional) Dataset for local testing

---

## 📊 Results
| Model | Accuracy | Features |
|--------|-----------|-----------|
| Logistic Regression | 92% | TF-IDF |
| XGBoost | 90% | TF-IDF |

---

## 🏆 Skills Demonstrated
- Natural Language Processing (NLP)
- Text Preprocessing
- TF-IDF Vectorization
- Logistic Regression, XGBoost
- Streamlit App Development
- Model Deployment (Hugging Face)

---

