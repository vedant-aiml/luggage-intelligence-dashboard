import streamlit as st
import pandas as pd

# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Luggage Intelligence", layout="wide")

# -------------------
# Load data
# -------------------
df = pd.read_csv("data/processed/cleaned_data.csv")

# -------------------
# Sidebar Filters (IMPORTANT)
# -------------------
st.sidebar.header("🔧 Filters")

selected_brands = st.sidebar.multiselect(
    "Select Brands",
    df["brand"].unique(),
    default=df["brand"].unique()
)

min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.5)

# Apply filters
df = df[(df["brand"].isin(selected_brands)) & (df["rating"] >= min_rating)]

# -------------------
# Title
# -------------------
st.title("🧳 Luggage Market Intelligence Dashboard")
st.caption("Analyze pricing, sentiment, and customer perception across brands")

# -------------------
# Overview
# -------------------
st.header("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Brands", df["brand"].nunique())
col2.metric("Total Products", df["product_name"].nunique())
col3.metric("Total Reviews", len(df))

# -------------------
# Brand Summary
# -------------------
st.header("🏷️ Brand Comparison")

brand_summary = df.groupby("brand").agg({
    "price": "mean",
    "rating": "mean",
    "discount_pct": "mean",
    "sentiment": "mean",
    "value_score": "mean"
}).reset_index()

brand_summary = brand_summary.round(2)
brand_summary = brand_summary.sort_values(by="value_score", ascending=False)

st.dataframe(brand_summary, use_container_width=True)

# -------------------
# Key Insight
# -------------------
st.subheader("📌 Key Insight")

top_brand = brand_summary.iloc[0]["brand"]
st.success(f"🏆 {top_brand} offers the best value for money based on sentiment and pricing.")

# -------------------
# Who is Winning & Why
# -------------------
st.header("🏆 Who is Winning & Why")

best = brand_summary.iloc[0]
premium = brand_summary.loc[brand_summary["price"].idxmax()]
discount = brand_summary.loc[brand_summary["discount_pct"].idxmax()]

st.markdown(f"""
### 🥇 Winner: **{best['brand']}**

**Why?**
- Sentiment: {best['sentiment']}
- Avg Price: ₹{best['price']}
- High value score → strong perceived value

---

### 💎 Premium Brand: **{premium['brand']}**
- Highest price: ₹{premium['price']}
- Sentiment: {premium['sentiment']}
- {"Customers justify premium pricing" if premium['sentiment'] > brand_summary['sentiment'].mean() else "Premium not strongly justified"}

---

### 💸 Discount Strategy: **{discount['brand']}**
- Highest discount: {discount['discount_pct']}%
- Competes aggressively on price
""")

# -------------------
# Charts
# -------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Price Comparison")
    st.bar_chart(brand_summary.set_index("brand")["price"])

with col2:
    st.subheader("😊 Sentiment Comparison")
    st.bar_chart(brand_summary.set_index("brand")["sentiment"])

# -------------------
# Theme Insights (🔥 BONUS)
# -------------------
st.header("🧠 Customer Review Themes")

theme_counts = df["themes"].str.split(", ").explode().value_counts()
st.bar_chart(theme_counts)

# Theme sentiment
st.subheader("Theme Sentiment")

theme_df = df.copy()
theme_df["theme"] = theme_df["themes"].str.split(", ")
theme_df = theme_df.explode("theme")

theme_sentiment = theme_df.groupby("theme")["sentiment"].mean().sort_values()

st.dataframe(theme_sentiment)

# -------------------
# Product Drilldown
# -------------------
st.header("🔍 Product Explorer")

selected_brand = st.selectbox("Select Brand", df["brand"].unique())

filtered_df = df[df["brand"] == selected_brand]

st.dataframe(filtered_df[[
    "product_name",
    "price",
    "rating",
    "sentiment",
    "themes"
]], use_container_width=True)

# -------------------
# Anomaly Detection (🔥 VERY IMPRESSIVE)
# -------------------
st.header("⚠️ Hidden Issues")

problem_products = df[(df["rating"] > 4) & (df["sentiment"] < 0.2)]

st.write("Products with high ratings but negative sentiment:")
st.dataframe(problem_products[[
    "brand", "product_name", "rating", "sentiment", "themes"
]])

# -------------------
# AI Insights
# -------------------
st.header("🤖 Agent Insights")

best_value = brand_summary.iloc[0]
worst_sentiment = brand_summary.loc[brand_summary["sentiment"].idxmin()]
highest_discount = brand_summary.loc[brand_summary["discount_pct"].idxmax()]

st.write(f"• 🏆 {best_value['brand']} delivers the best value for money.")
st.write(f"• ⚠️ {worst_sentiment['brand']} has the weakest customer sentiment.")
st.write(f"• 💸 {highest_discount['brand']} depends heavily on discounting.")

st.write("• 📊 Higher sentiment often justifies premium pricing.")
st.write("• 🧠 Theme analysis reveals strengths (durability) and weaknesses (zippers, handles).")