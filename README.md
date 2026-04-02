# 🧳 Luggage Market Intelligence Dashboard

---

## 📌 Overview

This project builds a **competitive intelligence dashboard** for luggage brands on Amazon India.
It transforms raw product and review data into **actionable insights** to identify:

* Which brand is winning
* Why customers prefer certain brands
* How pricing, discounts, and sentiment interact

---

## 🚀 Key Features

### 📊 Data Analysis

* Sentiment analysis on customer reviews
* Discount percentage calculation
* Value Score (Sentiment per ₹)
* Brand-level aggregation

### 🧠 Insight Engine

* Identifies **winning brand based on value**
* Detects **premium vs discount-driven strategies**
* Extracts **review themes** (durability, zipper, space, etc.)
* Performs **anomaly detection** (high rating but negative sentiment)

### 📈 Interactive Dashboard

* Built using **Streamlit**
* Brand & rating filters
* Product-level drilldown
* Theme and sentiment analysis
* Clean and intuitive UI

---

## 🏆 Key Insights

* **Aristocrat** delivers the best value despite premium pricing
* **Safari** relies heavily on discounting (price-driven strategy)
* **American Tourister** shows weaker sentiment signals
* **Durability** is a key strength across brands
* **Zippers and handles** are common complaint areas

---

## 🛠️ Tech Stack

* **Python** (Pandas, TextBlob)
* **Streamlit** (Dashboard)
* **Data Analysis & NLP**

---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run data processing
python analysis/sentiment_analysis.py

# Launch dashboard
streamlit run app/app.py
```

---

## 📁 Project Structure

```
luggage_dashboard/
│── data/
│   ├── raw/
│   └── processed/
│
│── analysis/
│   └── sentiment_analysis.py
│
│── app/
│   └── app.py
│
│── requirements.txt
│── README.md
```

---
## 🧱 Architecture

Raw Data (CSV)
→ Data Cleaning & Preprocessing
→ Sentiment Analysis (TextBlob)
→ Feature Engineering (discount %, value score, themes)
→ Aggregation & Insights
→ Streamlit Dashboard (UI + Filters + Visualizations)

---
## ⚠️ Limitations

* Dataset is limited and not scraped at scale
* Sentiment analysis uses TextBlob (basic NLP model)
* Theme extraction is keyword-based, not ML-driven
* No real-time data updates



---

## 🔮 Future Improvements

* Advanced NLP models (BERT / LLM-based sentiment)
* Real-time scraping pipeline
* Enhanced UI using Plotly
* Review trust & fake review detection
* Add real-time dashboard updates
* Improve theme extraction using clustering or embeddings
* Detect fake or biased reviews

---

## 🎯 Outcome

This dashboard goes beyond basic metrics and provides:

* **Decision-ready insights**
* Clear identification of **winning brands**
* Understanding of **customer perception vs pricing**

---

## 👨‍💻 Author

**Vedant Shinde**
GitHub: https://github.com/vedant-aiml
