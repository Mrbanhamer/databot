import requests
from main_menu.menu import main_menu

class reddit:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.url = f'https://www.reddit.com/r/{subreddit}/.json'
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/114.0.0.0 Safari/537.36"
        }    
    def url_source(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            post_list = []
            for post in posts:
                url_post = post['data']['url']        # external URL or self-post
                title = post['data']['title']
                permalink = post['data']['permalink']  # Reddit comment thread
                post_list.append({
                    "title": title,
                    "url": url_post,
                    "permalink": permalink
                })
            return post_list


def reddit_posts():
    subreddit_name = main_menu()
    if subreddit_name == 'None':
        exit()
    scraper = reddit(subreddit_name)
    posts = scraper.url_source()  # already a list of dicts with title, url, permalink
    return posts


if __name__ == '__main__':
    reddit_posts()

