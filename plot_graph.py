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

ax1.bar(x - width/2, post_scores, width, label="Post upvotes")
ax1.bar(x + width/2, comment_scores, width, label="Comments")

ax1.set_xlabel("Top 10 posts (rank)")
ax1.set_ylabel("Number of upvotes & comments")
ax1.legend(loc="upper left")

plt.title("Post upvotes and comments")
plt.show()

# -----------------------------
# SEPARATE ENGAGEMENT GRAPH
# -----------------------------
avg_engagement = sum(engagement_ratio) / len(engagement_ratio)

plt.figure(figsize=(8, 4))
plt.plot(x, engagement_ratio, marker="o", label="Engagement ratio")
plt.axhline(avg_engagement, linestyle="--", label=f"Average: {avg_engagement:.3f}")

plt.xlabel("Top 10 posts (rank)")
plt.ylabel("Engagement ratio (comments per post like)")
plt.title("Engagement ratio per post")
plt.grid(True)
plt.legend()
plt.savefig("engagement_plot.png", dpi=300, bbox_inches="tight")
plt.show()
