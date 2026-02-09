import json
from pathlib import Path
from bot.reddit_children_connector import child_url_post

JSON_PATH = Path(__file__).parent / "posts.json"


def save_posts_unique() -> None:
    # Get posts with comments data
    new_posts = child_url_post()

    # Load existing posts if file exists
    if JSON_PATH.exists():
        existing_posts = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    else:
        existing_posts = []

    # Use permalink as unique id (fallback to url)
    def unique_key(post: dict) -> str:
        return post.get("permalink") or post.get("url") or ""

    existing_keys = {unique_key(post) for post in existing_posts}

    # Add only new posts
    for post in new_posts:
        key = unique_key(post)
        if key and key not in existing_keys:
            existing_posts.append(post)
            existing_keys.add(key)

    # Save to JSON
    JSON_PATH.write_text(
        json.dumps(existing_posts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    save_posts_unique()
    print(f"Saved unique posts to {JSON_PATH}")