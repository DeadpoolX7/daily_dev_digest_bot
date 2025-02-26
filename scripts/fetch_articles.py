import feedparser
import json
from config import RSS_FEEDS

def fetch_articles():
    articles = []
    for url in RSS_FEEDS["articles"]:
        feed = feedparser.parse(url)
        for entry in feed.entries[:7]:
            articles.append({"title": entry.title, "link": entry.link})

    with open("data/articles.json", "w") as f:
        json.dump(articles, f, indent=4)

    return articles

if __name__ == "__main__":
    print(fetch_articles())
