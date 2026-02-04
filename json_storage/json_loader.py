import json
from pathlib import Path
from bot.reddit_connector import reddit_posts

JSON_PATH = Path(__file__).parent / "posts.json"

def save_posts_unique() -> None:
    new_posts = reddit_posts()  # list[{"title": ..., "url": ...}]

    if JSON_PATH.exists():
        existing_posts = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    else:
        existing_posts = []

    existing_urls = {post["url"] for post in existing_posts}

    for post in new_posts:
        if post["url"] not in existing_urls:
            existing_posts.append(post)

    JSON_PATH.write_text(
        json.dumps(existing_posts, ensure_ascii=False, indent=2),
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
    save_posts_unique()
    print(f"Saved unique posts to {JSON_PATH}")
