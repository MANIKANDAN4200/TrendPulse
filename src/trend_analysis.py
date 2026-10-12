import pandas as pd


# Load categorized data
df = pd.read_csv("data/hackernews_categorized.csv")


# Remove "other" category for our main analysis
analysis_df = df[df["category"] != "other"].copy()


# Category analysis
category_analysis = (
    analysis_df
    .groupby("category")
    .agg(
        stories=("id", "count"),
        average_score=("score", "mean"),
        average_comments=("comments", "mean")
    )
    .reset_index()
)


# Calculate Trend Score
category_analysis["trend_score"] = (
    category_analysis["average_score"]
    + category_analysis["average_comments"] * 2
)


# Sort by trend score
category_analysis = category_analysis.sort_values(
    by="trend_score",
    ascending=False
)


# Display results
print("\n===== TREND ANALYSIS =====\n")

print(category_analysis.to_string(index=False))


# Save analysis
category_analysis.to_csv(
    "data/trend_analysis.csv",
    index=False
)


print("\nAnalysis completed!")
print("Saved to: data/trend_analysis.csv")