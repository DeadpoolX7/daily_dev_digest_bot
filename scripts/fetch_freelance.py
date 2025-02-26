import feedparser
import json
from config import RSS_FEEDS

def fetch_freelance():
    gigs = []
    for url in RSS_FEEDS["freelance"]:
        feed = feedparser.parse(url)
        for entry in feed.entries[:7]:
            gigs.append({"title": entry.title, "link": entry.link})

    with open("data/freelance.json", "w") as f:
        json.dump(gigs, f, indent=4)

    return gigs

if __name__ == "__main__":
    print(fetch_freelance())
