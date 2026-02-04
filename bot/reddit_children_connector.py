import requests
from bot.reddit_connector import reddit_posts  # your existing import


def child_url_post():
    headers = {'User-Agent': 'my-reddit-scraper/1.2 (learning project)'}
    posts = reddit_posts()
    post_info_list = []

    print("Total posts returned:", len(posts))

    for post in posts:
        title = post.get('title', 'No Title')
        permalink = post.get('permalink')

        # Skip posts without a permalink (likely not a proper Reddit post)
        if not permalink:
            print(f"Skipped post without permalink: {title}")
            continue

        # Construct the Reddit post URL from the permalink
        reddit_post_url = "https://www.reddit.com" + permalink
        print(f"\nFetching Reddit post: {reddit_post_url}")

        json_url = reddit_post_url.rstrip('/') + '.json'

        try:
            response = requests.get(json_url, headers=headers)
            if response.status_code != 200:
                print(f"Failed request ({response.status_code}) for {reddit_post_url}")
                continue
        except Exception as e:
            print(f"Request failed for {reddit_post_url}: {e}")
            continue

        try:
            data = response.json()

            # --- Post data ---
            post_data = data[0]['data']['children'][0]['data']
            upvotes = post_data.get('ups', 0)
            comment_count = post_data.get('num_comments', 0)

            # --- Top-level comments ---
            comments = {}
            comment_listing = data[1]['data']['children']

            for item in comment_listing:
                if item['kind'] == 't1':  # t1 = comment
                    comment_data = item['data']
                    comment_id = comment_data['id']
                    comment_body = comment_data.get('body', '')
                    comments[comment_id] = comment_body

            # --- Build post dictionary ---
            post_info = {
                'title': title,
                'url': reddit_post_url,  # Always Reddit URL
                'upvotes': upvotes,
                'comment_count': comment_count,
                'comments': comments
            }

            print(f"Collected: {title} ({len(comments)} top-level comments)")
            post_info_list.append(post_info)

        except Exception as e:
            print(f"Failed to parse JSON for {reddit_post_url}: {e}")

    print("\nFinal list of posts with comments collected:")
    return post_info_list


if __name__ == '__main__':
    posts_with_comments = child_url_post()
    for post in posts_with_comments:
        print(post)
