from reddit_connector import redditconnect

for submission in redditconnect.subreddit('mildyinteresting').top(limit=10):
    print(submission.title)