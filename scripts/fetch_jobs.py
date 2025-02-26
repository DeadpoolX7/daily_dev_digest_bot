import feedparser
import json
from config import RSS_FEEDS

def fetch_jobs():
    jobs = []
    for url in RSS_FEEDS["jobs"]:
        feed = feedparser.parse(url)
        for entry in feed.entries[:7]:  # Get top 7
            jobs.append({"title": entry.title, "link": entry.link})
    
    with open("data/jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

    return jobs

if __name__ == "__main__":
    print(fetch_jobs())
