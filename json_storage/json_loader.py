import json
from bot.reddit_connector import reddit_posts

def save_posts_to_json():
    titles, urls = reddit_posts()

    data = []
    for title, url in zip(titles, urls):
        data.append({"title": title, "url": url})

    with open("json_storage/posts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save_posts_to_json()
