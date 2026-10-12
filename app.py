import streamlit as st
import pandas as pd


# Page configuration
st.set_page_config(
    page_title="TrendPulse",
    page_icon="📈",
    layout="wide"
)


# Title
st.title("📈 TrendPulse")
st.subheader("Hacker News Trending Topics Dashboard")


# Load data
df = pd.read_csv("data/hackernews_categorized.csv")
analysis_df = pd.read_csv("data/trend_analysis.csv")


# Remove "other"
analysis_df = analysis_df[
    analysis_df["category"] != "other"
]


# Dashboard metrics
total_stories = len(df)
total_categories = analysis_df["category"].nunique()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Stories", total_stories)

with col2:
    st.metric("Categories", total_categories)


st.divider()


# Category filter
st.subheader("🔎 Filter Stories")

categories = analysis_df["category"].tolist()

selected_category = st.selectbox(
    "Select a category",
    ["All"] + categories
)


if selected_category == "All":
    filtered_df = df[
        df["category"] != "other"
    ]
else:
    filtered_df = df[
        df["category"] == selected_category
    ]


# Show stories
st.subheader("📰 Trending Stories")

st.dataframe(
    filtered_df[
        ["title", "author", "score", "comments", "category"]
    ],
    use_container_width=True
)


st.divider()


# Category analysis
st.subheader("📊 Category Analysis")

st.dataframe(
    analysis_df,
    use_container_width=True
)


# Charts
st.subheader("📈 Trend Charts")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "data/stories_by_category.png",
        caption="Stories by Category"
    )

with col2:
    st.image(
        "data/trend_score_by_category.png",
        caption="Trend Score by Category"
    )

st.success("TrendPulse dashboard loaded successfully!")