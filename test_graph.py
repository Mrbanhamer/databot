import matplotlib.pyplot as plt
import numpy as np

#Fake data to simulate reddit comments etc

#Likes on top 10 
post_scores = [1200, 980, 1500, 700, 430, 860, 300, 1100, 640, 520]

#Total likes on comments
comment_scores = [400, 350, 600, 200, 90, 300, 60, 500, 180, 140]

#Correlation
correlation = np.corrcoef(post_scores, comment_scores)[0, 1]
print("Correlation coefficient:", round(correlation, 2))

#Engagment ratio
#engagement_ratio = [c/p if p != 0 else 0 for c, p in zip(comment_scores, post_scores)]
#print("\nEngagement ratio (comment likes per post like) per post:")
#for i, ratio in enumerate(engagement_ratio, start=1):
#    print(f"post {i}: {ratio:.2f}")

#visual
x = np.arange(1, 11)
width = 0.25

#Bar chart
plt.bar(x - width / 2, post_scores, width, label="Post upvotes")
plt.bar(x + width / 2, comment_scores, width, label="Comment upvotes")

#plt.bar(x + width, [r * 100 for r in engagement_ratio], width, label="Engagement ratio (%)")

#title
plt.xlabel("Top 10 posts (rank)")
plt.ylabel("Number of upvotes")
plt.title("Test graph: Post upvotes vs Comment upvotes")

plt.legend()

#Show graph
plt.show()
