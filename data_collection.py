import requests
import pandas as pd

# NewsAPI key
API_KEY = "your_api_key"
URL = "https://newsapi.org/v2/top-headlines"

# Parameters
params = {
    "country": "us",        # change to "in" for India
    "category": "technology",
    "pageSize": 100,        
    "apiKey": API_KEY
}

# API call
response = requests.get(URL, params=params)
data = response.json()

# Extract articles
articles = data.get("articles", [])

# Convert to DataFrame
df = pd.DataFrame(articles)

# Show only headlines
print("\n News Headlines\n")
for i, title in enumerate(df["title"], start=1):
    print(f"{i}. {title}")

# Save to CSV
df.to_csv("news_headlines.csv", index=False)

