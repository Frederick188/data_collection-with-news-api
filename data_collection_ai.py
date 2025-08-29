from newsapi import NewsApiClient
import pandas as pd

# Initialize News API Client
newsapi = NewsApiClient(api_key="b72173ad99a44841b9711f489cff881e")

# Fetch AI-related news
ai_news = newsapi.get_everything(
    q="artificial intelligence",   # query keyword
    language="en",                 # language
    sort_by="publishedAt",         # latest news first
    page_size=100                  # max results per request
)

# Extract articles
articles = ai_news.get("articles", [])

# Convert to DataFrame
df = pd.DataFrame(articles)

print("\nArtificial Intelligence News Headlines\n")
for i, title in enumerate(df["title"], start=1):
    print(f"{i}. {title}")

# Save to CSV
df.to_csv("ai_news_headlines.csv", index=False)
