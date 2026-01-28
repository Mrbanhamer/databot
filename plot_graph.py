import json
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# LOAD DATA FROM JSON
# -----------------------------
with open("reddit_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

post_scores = [d["post_upvotes"] for d in data]
comment_scores = [d["comment_upvotes"] for d in data]
engagement_ratio = [d["engagement_ratio"] for d in data]

# -----------------------------
# CREATE GRAPH
# -----------------------------
x = np.arange(1, len(post_scores) + 1)
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 5))

# Left axis: upvotes
ax1.bar(x - width/2, post_scores, width, label="Post upvotes")
ax1.bar(x + width/2, comment_scores, width, label="Comment upvotes")
ax1.set_xlabel("Top 10 posts (rank)")
ax1.set_ylabel("Number of upvotes")
ax1.legend(loc="upper left")

# Right axis: engagement ratio
ax2 = ax1.twinx()
ax2.plot(x, engagement_ratio, marker="o", label="Engagement ratio")
ax2.set_ylabel("Engagement ratio (comment likes per post like)")
ax2.legend(loc="upper right")

plt.title("Post upvotes, Comment upvotes, and Engagement ratio")
plt.show()