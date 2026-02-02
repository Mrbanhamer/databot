from bot.reddit_connector import reddit_posts

#this module will take in name of reddit posts and the url link of them in a list

print(reddit_posts())

def child_url_post():
    url_sorter = reddit_posts()
    for url in url_sorter:
        if url.startswith('https://www.reddit.com'):
            source_url = url
        else:
            post_title = url
    
