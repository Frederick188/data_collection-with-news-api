from newsapi import NewsApiClient
import pandas as pd

# Init
newsapi = NewsApiClient(api_key="your_api_key") 

# Fetch top headlines
top_headlines = newsapi.get_top_headlines(
    country="us",          # change to "in" for India
    category="technology",
    page_size=100,
    language="en"
)

# Extract articles
articles = top_headlines.get("articles", [])

# Convert to DataFrame
df = pd.DataFrame(articles)

print("\n News Headlines\n")
for i, title in enumerate(df["title"], start=1):
    print(f"{i}. {title}")

# Save to CSV
df.to_csv("news_headlines.csv", index=False)
