import requests

url = "https://www.reddit.com/r/mildlyinteresting/.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"]
        url_post = post["data"]["url"]
        print(title, "-", url_post)
else:
    print("Failed to get JSON. Response text:")
    print(response.text[:500])  # show first 500 characters

def show500():
    url = "https://www.reddit.com/r/mildlyinteresting/.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            url_post = post["data"]["url"]
            return title, "-", url_post
    else:
        return "Failed to get JSON. Response text:"
        return response.text[:500]  # show first 500 characters