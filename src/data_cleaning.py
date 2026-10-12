import pandas as pd

# Load raw data
df = pd.read_csv("data/hackernews_raw.csv")

print("Original data:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# Remove rows without a title
df = df.dropna(subset=["title"])

# Remove duplicate stories
df = df.drop_duplicates(subset=["id"])

# Convert Unix timestamp to readable date/time
df["time"] = pd.to_datetime(df["time"], unit="s")


# Save cleaned data
df.to_csv("data/hackernews_cleaned.csv", index=False)

print("\nData cleaning completed!")
print(f"Cleaned stories: {len(df)}")
print("Saved to: data/hackernews_cleaned.csv")