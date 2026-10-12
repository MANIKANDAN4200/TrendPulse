import pandas as pd


# Load cleaned data
df = pd.read_csv("data/hackernews_cleaned.csv")


# Category keywords
categories = {
    "technology": [
        "ai", "software", "computer", "python",
        "programming", "google", "microsoft",
        "apple", "robot", "technology",
        "cybersecurity", "chip", "internet"
    ],

    "worldnews": [
        "war", "government", "president",
        "election", "politics", "ukraine",
        "russia", "china", "india",
        "iran", "israel", "minister"
    ],

    "sports": [
        "football", "cricket", "tennis",
        "basketball", "soccer", "olympics",
        "fifa", "ipl", "player",
        "match", "team", "championship"
    ],

    "science": [
        "science", "space", "nasa",
        "research", "physics", "biology",
        "chemistry", "planet", "climate",
        "scientist", "discovery"
    ],

    "entertainment": [
        "movie", "film", "actor", "actress",
        "music", "song", "netflix",
        "hollywood", "bollywood",
        "celebrity", "series", "concert", "tv"
    ]
}


# Function to categorize a story
def categorize_story(title):

    title = title.lower()

    for category, keywords in categories.items():

        for keyword in keywords:

            if keyword in title:
                return category

    return "other"


# Apply categorization
df["category"] = df["title"].apply(categorize_story)


# Save categorized data
df.to_csv("data/hackernews_categorized.csv", index=False)


print("Categorization completed!")

print("\nCategory counts:")
print(df["category"].value_counts())

print("\nSaved to:")
print("data/hackernews_categorized.csv")