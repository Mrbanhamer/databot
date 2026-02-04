import requests
from bot.reddit_connector import reddit_posts
from json_storage.json_loader import save_titles

def child_url_post():
    headers = {
        'User-Agent': 'my-reddit-scraper/1.2 (learning project)'
    }
    posts = reddit_posts()
    post_info_list = []  # List to store dictionaries for each post

    for post in posts:
        url = post['url']
    
    # Only attempt JSON request if the URL is a reddit post
        if url.startswith('https://www.reddit.com/r/'):
            json_url = url + '.json'
            response = requests.get(json_url, headers=headers)

            if response.status_code == 200:
                try:
                    data = response.json()
                    post_data = data[0]['data']['children'][0]['data']
                    upvotes = post_data.get('ups', 0)
                    comments = post_data.get('num_comments', 0)

                    post_info = {
                        'title': post['title'],
                        'url': url,
                        'upvotes': upvotes,
                        'comments': comments
                    }

                    post_info_list.append(post_info)
                except Exception as e:
                    print(f'Failed to parse JSON for {url}:', e)
            else:
                print(f'Failed request for {url}: {response.status_code}')
        else:
            print(f'Skipping non-reddit URL: {url}')

    # Optional: save or print the list of post info
    return post_info

if __name__ == '__main__':
    child_url_post()
