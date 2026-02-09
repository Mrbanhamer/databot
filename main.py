#you start this file to start the entire program
from json_storage.json_loader import save_posts_unique
from graphs.plot__graph import plot_reddit_engagement

if __name__ == '__main__':
    save_posts_unique()
    plot_reddit_engagement()