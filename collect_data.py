import requests
import json
import logging

# Logger for successful runs
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Separate logger for errors
error_logger = logging.getLogger("error_logger")
error_handler = logging.FileHandler("errors.log")
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
error_handler.setFormatter(formatter)

error_logger.addHandler(error_handler)



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
        logging.info(f"Starting data collection for subreddit: {self.subreddit}")

        # 1) HTTP request
        response = requests.get(self.url, headers=self.headers)

        # 2) Handle common error
        if response.status_code == 404:
            message = f"Subreddit r/{self.subreddit} does not exist (404)."
            print(message)
            error_logger.error(message)
            return


        if response.status_code == 403:
            print(f"Subreddit r/{self.subreddit} is private or forbidden (403).")
            print(message)
            error_logger.error(message)
            return

        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            print(message)
            error_logger.error(message)
            error_logger.error(response.text[:300])
            return

        # 3) Parse JSON safely
        data = response.json()
        posts = data["data"]["children"]

        # 4) Handle empty subreddit
        if not posts:
            print(f"No posts found in r/{self.subreddit}.")
            print(message)
            error_logger.error(message)
            return
        # 5) Collect data
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

        # 6) Save to JSON only if we actually collected something
        if not collected_data:
            print("No data collected, JSON will not be written.")
            return

        with open("reddit_data.json", "w", encoding="utf-8") as f:
            json.dump(collected_data, f, indent=2)

        print("reddit_data.json created successfully")

        logging.info(
            f"Successfully collected {len(collected_data)} posts "
            f"from r/{self.subreddit} and saved to reddit_data.json"
        )



if __name__ == "__main__":

    subreddit_name = input("Write a subreddit: ")
    scraper = RedditScraper(subreddit_name)
    scraper.collect()