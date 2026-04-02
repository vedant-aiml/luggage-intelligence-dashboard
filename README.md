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

```
     ┌────────────────────┐
     │   Raw Data (CSV)   │
     └─────────┬──────────┘
               │
               ▼
     ┌──────────────────────────────┐
     │ Data Cleaning & Preprocessing│
     └─────────┬────────────────────┘
               │
               ▼
     ┌──────────────────────────────┐
     │ Sentiment Analysis (TextBlob)│
     └─────────┬────────────────────┘
               │
               ▼
     ┌──────────────────────────────┐
     │ Feature Engineering          │
     │ - Discount %                 │
     │ - Value Score                │
     │ - Themes Extraction          │
     └─────────┬────────────────────┘
               │
               ▼
     ┌──────────────────────────────┐
     │ Aggregation & Insights       │
     └─────────┬────────────────────┘
               │
               ▼
     ┌──────────────────────────────┐
     │ Streamlit Dashboard          │
     │ UI + Filters + Visualizations│
     └──────────────────────────────┘
```
---
# 📊 Sentiment Analysis Dashboard

A dashboard to analyze brand sentiment and compare insights using data visualization.

🌐 **Live Demo:** [Click here to view the live dashboard](App link :https://luggage-intelligence-dashboard-3cehypb9ftovmrmgwjizhg.streamlit.app/)

---
## 🎥 Project Walkthrough

 [![Watch the demo](https://cdn.loom.com/sessions/thumbnails/f46d79fd946f4bb7b94174cbccbac7f8-with-play.gif)](https://www.loom.com/share/vf46d79fd946f4bb7b94174cbccbac7f8)

⏱️ Video Sections (Timestamps)

1. Introduction (0:00 – 0:30)
Brief overview of the project
Purpose of the dashboard
2. Dataset Overview (0:30 – 1:30)
What data is used
Key features/columns
3. Dashboard Overview (1:30 – 3:00)
Layout explanation
Key components (charts, filters, KPIs)
4. Key Insights (3:00 – 4:30)
Sentiment trends
Brand comparison highlights
5. Code Explanation (Optional) (4:30 – 5:30)
Brief explanation of logic
Tools/libraries used
6. Conclusion (5:30 – End)
Summary of project
Final thoughts
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
