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

#    def connect(self):
#        response = requests.get(self.url, headers=self.headers)
#        if response.status_code == 200:
#            data = response.json()
#          posts = data["data"]["children"]
#            for post in posts:
#                title = post["data"]["title"]
#                url_post = post["data"]["url"]
#                reddit_link = "https://www.reddit.com" + post["data"]["permalink"]
#                print(title)
#                print("Post URL:", reddit_link)
#                print("Direct URL:", url_post)
#                print("-" * 50)
#        else:
#            print("Failed to get JSON. Response text:")
#            print(response.text[:500])  # show first 500 characters
    
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
                url_temp.append("https://www.reddit.com" + url_post)    
            return post_title, url_temp

def reddit_posts():
    subreddit_name = main_menu()
    if subreddit_name == 'None':
        exit()
    scraper = reddit(subreddit_name)
    scraper.url_source()

if __name__ == '__main__':
    subreddit_name = main_menu()
    if subreddit_name == 'None':
        exit()
    scraper = reddit(subreddit_name)
    scraper.connect()