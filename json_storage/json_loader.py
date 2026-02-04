import json
from pathlib import Path
from bot.reddit_connector import reddit_posts

JSON_PATH = Path(__file__).parent / "posts.json"

def save_posts(posts: list[dict]) -> None:
    JSON_PATH.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def save_titles() -> None:
    posts = reddit_posts()
    titles = [post["title"] for post in posts]
    JSON_PATH.write_text(
        json.dumps(titles, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

if __name__ == "__main__":
    # saves full posts (title + url)
    posts = reddit_posts()
    save_posts(posts)
    print(f"Saved {len(posts)} posts to {JSON_PATH}")