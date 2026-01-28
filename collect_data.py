import json

#-----------------------------
#MOCK DATA (temporary test data)
#-----------------------------
post_scores = [1200, 980, 1500, 700, 430, 860, 300, 1100, 640, 520]
comment_scores = [400, 350, 600, 200, 90, 300, 60, 500, 180, 140]

#-----------------------------
#STRUCTURE DATA FOR JSON
#-----------------------------
data = []

for i in range(len(post_scores)):
    data.append({
        "post_rank": i + 1,
        "post_upvotes": post_scores[i],
        "comment_upvotes": comment_scores[i],
        "engagement_ratio": comment_scores[i] / post_scores[i]
    })

#-----------------------------
#SAVE TO JSON FILE
#-----------------------------
with open("reddit_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("reddit_data.json created successfully")