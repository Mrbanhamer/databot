from bot.reddit_connector import reddit_posts
from json_storage.json_loader import save_titles

#this module will take in name of reddit posts and the url link of them in a list

print(reddit_posts())



def child_url_post():
    posts = reddit_posts()
    for post in posts:
        print(post['url'])
        print(post['title'])

if __name__ == '__main__':
    child_url_post()