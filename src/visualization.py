import pandas as pd
import matplotlib.pyplot as plt


# Load trend analysis data
df = pd.read_csv("data/trend_analysis.csv")


# -----------------------------
# Chart 1: Number of Stories
# -----------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["category"], df["stories"])

plt.title("Number of Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("data/stories_by_category.png")

plt.show()


# -----------------------------
# Chart 2: Average Score
# -----------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["category"], df["average_score"])

plt.title("Average Hacker News Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("data/average_score_by_category.png")

plt.show()


# -----------------------------
# Chart 3: Trend Score
# -----------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["category"], df["trend_score"])

plt.title("Trend Score by Category")
plt.xlabel("Category")
plt.ylabel("Trend Score")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("data/trend_score_by_category.png")

plt.show()


print("Visualization completed!")
print("Charts saved inside the data folder.")