import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_reddit_engagement(
    json_path: str | Path = "json_storage/posts.json",
    save_engagement_plot: bool = True,
    output_path: str | Path = "engagement_plot.png"
) -> None:
    """
    Loads Reddit post data from JSON and plots:
    1) Post upvotes vs comment count (bar chart)
    2) Engagement ratio per post (comments / upvotes)
    """

    json_path = Path(json_path)

    # -----------------------------
    # LOAD DATA FROM JSON
    # -----------------------------
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    post_scores = []
    comment_scores = []
    engagement_ratio = []

    for d in data:
        upvotes = d.get("upvotes", 0)
        comments = d.get("comment_count", 0)

        post_scores.append(upvotes)
        comment_scores.append(comments)

        # Avoid division by zero
        if upvotes > 0:
            engagement_ratio.append(comments / upvotes)
        else:
            engagement_ratio.append(0)

    # -----------------------------
    # CREATE BAR GRAPH
    # -----------------------------
    x = np.arange(1, len(post_scores) + 1)
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.bar(x - width / 2, post_scores, width, label="Post upvotes")
    ax1.bar(x + width / 2, comment_scores, width, label="Comments")

    ax1.set_xlabel("Top posts (rank)")
    ax1.set_ylabel("Number of upvotes & comments")
    ax1.legend(loc="upper left")

    plt.title("Post upvotes and comments")
    plt.show()

    # -----------------------------
    # ENGAGEMENT RATIO GRAPH
    # -----------------------------
    avg_engagement = sum(engagement_ratio) / len(engagement_ratio)

    plt.figure(figsize=(8, 4))
    plt.plot(x, engagement_ratio, marker="o", label="Engagement ratio")
    plt.axhline(avg_engagement, linestyle="--", label=f"Average: {avg_engagement:.3f}")

    plt.xlabel("Top posts (rank)")
    plt.ylabel("Engagement ratio (comments per upvote)")
    plt.title("Engagement ratio per post")
    plt.grid(True)
    plt.legend()

    if save_engagement_plot:
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.show()
