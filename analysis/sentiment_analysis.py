import pandas as pd
from textblob import TextBlob

# Load data
df = pd.read_csv("data/raw/data.csv", encoding="latin-1")

# Sentiment function
def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

# Apply sentiment
df["sentiment"] = df["review_text"].apply(get_sentiment)

# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

# Brand-level sentiment
brand_sentiment = df.groupby("brand")["sentiment"].mean()

print("\n=== Brand Sentiment ===")
print(brand_sentiment)

# Discount %
df["discount_pct"] = ((df["mrp"] - df["price"]) / df["mrp"]) * 100

# Value Score (VERY IMPORTANT)
df["value_score"] = df["sentiment"] / df["price"] * 1000

# Brand-level summary
brand_summary = df.groupby("brand").agg({
    "price": "mean",
    "rating": "mean",
    "discount_pct": "mean",
    "sentiment": "mean",
    "value_score": "mean",
    "review_count": "mean"
}).reset_index()

print("\n=== Brand Summary ===")
print(brand_summary)

# Theme keywords
themes = {
    "durability": ["durable", "sturdy", "strong", "weak", "break"],
    "wheels": ["wheel", "rolling"],
    "handle": ["handle"],
    "zipper": ["zip", "zipper", "chain"],
    "space": ["space", "capacity", "compartment"]
}

# Function to extract themes
def extract_themes(text):
    text = str(text).lower()
    found = []
    for theme, keywords in themes.items():
        for word in keywords:
            if word in text:
                found.append(theme)
                break
    return ", ".join(found)

# Apply theme extraction
df["themes"] = df["review_text"].apply(extract_themes)

print("\n=== Sample Themes ===")
print(df[["review_text", "themes"]].head())

print("\n=== Agent Insights ===")

insights = []

# Best value
best_value = brand_summary.loc[brand_summary["value_score"].idxmax()]
insights.append(f"{best_value['brand']} delivers the strongest value for money, combining high customer sentiment with its pricing.")

# Premium but justified
expensive = brand_summary.loc[brand_summary["price"].idxmax()]
if expensive["sentiment"] > brand_summary["sentiment"].mean():
    insights.append(f"{expensive['brand']} commands premium pricing but maintains strong customer satisfaction, indicating justified pricing.")
else:
    insights.append(f"{expensive['brand']} is priced at a premium but does not show proportionally high customer satisfaction.")

# Discount strategy
discount_brand = brand_summary.loc[brand_summary["discount_pct"].idxmax()]
insights.append(f"{discount_brand['brand']} relies heavily on discounting, suggesting a price-driven growth strategy.")

# Strongest sentiment
best_sentiment = brand_summary.loc[brand_summary["sentiment"].idxmax()]
insights.append(f"{best_sentiment['brand']} leads in customer sentiment, indicating strong product acceptance.")

# Weakest sentiment
worst_sentiment = brand_summary.loc[brand_summary["sentiment"].idxmin()]
insights.append(f"{worst_sentiment['brand']} shows weaker sentiment, which may indicate recurring product issues or unmet expectations.")

# Print
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")


# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("\n✅ Cleaned data saved to data/processed/cleaned_data.csv")
