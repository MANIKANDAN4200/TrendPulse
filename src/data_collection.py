
import pandas as pd
import urllib.request
import json
import time

BASE_URL = "https://hacker-news.firebaseio.com/v0"

HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}


def fetch_json(url):
    request = urllib.request.Request(
        url,
        headers=HEADERS
    )

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


# Step 1: Get top story IDs
print("Fetching top story IDs...")

story_ids = fetch_json(
    f"{BASE_URL}/topstories.json"
)

# Fetch first 500 stories
story_ids = story_ids[:500]

print(f"Found {len(story_ids)} stories.")


# Step 2: Get each story's details
stories = []

for count, story_id in enumerate(story_ids, start=1):

    try:
        story_url = f"{BASE_URL}/item/{story_id}.json"

        story = fetch_json(story_url)

        if story:
            stories.append(story)

        print(f"Fetched {count}/500")

        time.sleep(0.05)

    except Exception as error:
        print(f"Error fetching story {story_id}: {error}")


print("\nData collection completed.")
print(f"Successfully fetched: {len(stories)} stories")


# Show first story
if stories:
    print("\nFirst story:")
    print(stories[0])
    # Convert stories into a list of useful fields
clean_stories = []

for story in stories:
    clean_stories.append({
        "id": story.get("id"),
        "title": story.get("title"),
        "author": story.get("by"),
        "score": story.get("score", 0),
        "comments": story.get("descendants", 0),
        "time": story.get("time"),
        "url": story.get("url")
    })


# Create a DataFrame
df = pd.DataFrame(clean_stories)


# Save data to CSV
df.to_csv("data/hackernews_raw.csv", index=False)


print("\nCSV file created successfully!")
print(f"Saved {len(df)} stories to data/hackernews_raw.csv")