import requests
from bot.reddit_connector import reddit_posts
from json_storage.json_loader import save_titles

#this module will take in name of reddit posts and the url link of them in a list

#print(reddit_posts())

def child_url_post():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.0.0 Safari/537.36"
    }
    posts = reddit_posts()
    for post in posts:
        response = requests.get(post['url'], headers)
        if response.status_code == 200:
            data = response.json()
            upvotes = data['ups']
            print(upvotes)
        print(post['url'])
        print(post['title'])

if __name__ == '__main__':
    child_url_post()