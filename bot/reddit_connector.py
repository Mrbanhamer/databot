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
            post_title=[]
            url_temp=[]
            for post in posts:
                url_post = post['data']['url']
                title = post["data"]["title"]
                post_title.append(title)
                if url_post.startswith("http"):
                    full_url = url_post
                else:
                    full_url = "https://www.reddit.com" + url_post
                url_temp.append(full_url)
            return post_title, url_temp

def reddit_posts():
    subreddit_name = main_menu()
    if subreddit_name == 'None':
        exit()
    scraper = reddit(subreddit_name)
    titles, urls, = scraper.url_source()
    posts = [{"title": t, "url": u} for t, u in zip(titles, urls)]
    return posts

if __name__ == '__main__':
    reddit_posts()