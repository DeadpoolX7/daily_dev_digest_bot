import scripts.fetch_jobs as fetch_jobs
import scripts.fetch_freelance as fetch_freelance
import scripts.fetch_articles as fetch_articles
import scripts.update_readme as update_readme

def main():
    print("Fetching latest jobs...")
    fetch_jobs.fetch_jobs()

    print("Fetching latest freelance gigs...")
    fetch_freelance.fetch_freelance()

    print("Fetching latest tech articles...")
    fetch_articles.fetch_articles()

    print("Updating README.md...")
    update_readme.update_readme()

    print("✅ Daily Dev Digest updated successfully!")

if __name__ == "__main__":
    main()
