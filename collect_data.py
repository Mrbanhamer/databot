import requests
import json

class RedditScraper:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10&t=day"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36"
        }

    def collect(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code != 200:
            print("Failed to fetch data")
            print(response.text[:500])
            return

        data = response.json()
        posts = data["data"]["children"]

        collected_data = []

        for i, post in enumerate(posts):
            post_data = post["data"]

            post_upvotes = post_data["score"]
            comment_count = post_data["num_comments"]

            collected_data.append({
                "post_rank": i + 1,
                "post_upvotes": post_upvotes,
                "comment_upvotes": comment_count,
                "engagement_ratio": comment_count / post_upvotes if post_upvotes > 0 else 0
            })

        with open("reddit_data.json", "w", encoding="utf-8") as f:
            json.dump(collected_data, f, indent=2)

        print("reddit_data.json created successfully")


if __name__ == "__main__":

    subreddit_name = input("Write a subreddit: ")
    scraper = RedditScraper(subreddit_name)
    scraper.collect()