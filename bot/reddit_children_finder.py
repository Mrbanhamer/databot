import requests
from bot.reddit_connector import reddit_posts
from json_storage.json_loader import save_titles

#this module will take in name of reddit posts and the url link of them in a list


def child_url_post():
    headers = {
        'User-Agent': 'my-reddit-scraper/1.2 (learning project)'
    }
    posts = reddit_posts()
    for post in posts:
        # Make sure we request JSON
        json_url = post['url'] + ".json"
        response = requests.get(json_url, headers=headers)

        if response.status_code == 200:
            try:
                data = response.json()
                post_data = data[0]['data']['children'][0]['data']
                upvotes = post_data['ups']
                print(f"Upvotes: {upvotes}")
            except Exception as e:
                print("Failed to parse JSON:", e)
        else:
            print("Failed request:", response.status_code)

        print(post['url'])
        print(post['title'])


if __name__ == '__main__':
    child_url_post()