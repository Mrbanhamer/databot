import praw

reddit = praw.reddit(
    client_id = 'my client id',
    client_secret = 'my client secret',
    user_agent = 'my user agent',
)

for submission in reddit.subreddit('test').hot(limit=10):
    print(submission.title)