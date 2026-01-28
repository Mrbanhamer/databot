import matplotlib.pyplot as plt
import numpy as np

#-----------------------------
#MOCK DATA
#-----------------------------
post_scores = [1200, 980, 1500, 700, 430, 860, 300, 1100, 640, 520]
comment_scores = [400, 350, 600, 200, 90, 300, 60, 500, 180, 140]

#Calculate engagement ratio
engagement_ratio = [c/p if p != 0 else 0 for c, p in zip(comment_scores, post_scores)]

#-----------------------------
#GRAPH WITH TWO Y-AXES
#-----------------------------
x = np.arange(1, 11)
width = 0.35

fig, ax1 = plt.subplots(figsize=(10,5))

#Left axis: post likes and comment likes
ax1.bar(x - width/2, post_scores, width, label="Post upvotes", color="skyblue")
ax1.bar(x + width/2, comment_scores, width, label="Comment upvotes", color="lightgreen")
ax1.set_xlabel("Top 10 posts (rank)")
ax1.set_ylabel("Number of upvotes")
ax1.tick_params(axis='y')
ax1.legend(loc='upper left')

#Right axis: engagement ratio
ax2 = ax1.twinx()
ax2.plot(x, engagement_ratio, color="red", marker="o", label="Engagement ratio (comments/post)")
ax2.set_ylabel("Engagement ratio (comments per post like)")
ax2.tick_params(axis='y')
ax2.legend(loc='upper right')

plt.title("Post upvotes, Comment upvotes, and Engagement Ratio")
plt.show()
