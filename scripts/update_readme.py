import json

def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        return []

def update_readme():
    jobs = load_data("data/jobs.json")
    freelance = load_data("data/freelance.json")
    articles = load_data("data/articles.json")

    readme_content = "# 📢 Daily Dev Digest\n\n"
    readme_content += "### 💼 Latest Job Listings\n"
    for job in jobs:
        readme_content += f"- [{job['title']}]({job['link']})\n"
    
    readme_content += "\n### 🎯 Freelance Opportunities\n"
    for gig in freelance:
        readme_content += f"- [{gig['title']}]({gig['link']})\n"
    
    readme_content += "\n### 📝 Latest Tech Articles\n"
    for article in articles:
        readme_content += f"- [{article['title']}]({article['link']})\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()
