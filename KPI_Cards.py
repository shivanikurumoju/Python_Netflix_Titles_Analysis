import streamlit as st
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("titles_cleaned.csv")

# Calculate KPIs
total_titles = len(df)
total_movies = (df["type"] == "MOVIE").sum()
total_shows = (df["type"] == "SHOW").sum()
avg_imdb = df["imdb_score"].mean()

# Dashboard Title
st.title("🎬 Netflix Titles Dashboard")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Titles", total_titles)

with col2:
    st.metric("Movies", total_movies)

with col3:
    st.metric("TV Shows", total_shows)

with col4:
    st.metric("Average IMDb", round(avg_imdb, 2))

# Calculated KPIs 
avg_tmdb = df["tmdb_score"].mean()

avg_runtime = df["runtime"].mean()

latest_year = df["release_year"].max()

total_votes = df["imdb_votes"].sum()

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric("⭐ Average TMDb", round(avg_tmdb, 2))

with col6:
    st.metric("⏱ Average Runtime", round(avg_runtime, 2))

with col7:
    st.metric("📅 Latest Release", latest_year)

with col8:
    st.metric("👍 IMDb Votes", f"{total_votes:,.0f}")

import matplotlib.pyplot as plt
import seaborn as sns

col1, col2 = st.columns(2)

with col1:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="type")
    plt.title("Movies vs TV Shows")
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(6,4))
    sns.histplot(df["imdb_score"])
    plt.title("IMDb Distribution")
    st.pyplot(plt)

with col1:

    plt.figure(figsize=(6,4))

    genres = df["genres"].str.split(", ").explode()

    top_genres = genres.value_counts().head(10)

    sns.barplot(
        x=top_genres.values,
        y=top_genres.index
    )

    plt.title("Top 10 Genres")

    st.pyplot(plt)

with col2:

    plt.figure(figsize=(6,4))

    countries = df["production_countries"].str.split(", ").explode()

    top_countries = countries.value_counts().head(10)

    sns.barplot(
        x=top_countries.values,
        y=top_countries.index
    )

    plt.title("Top 10 Production Countries")

    st.pyplot(plt)   

col1, col2 = st.columns(2)

with col1:

    plt.figure(figsize=(6,4))

    yearly = df["release_year"].value_counts().sort_index()

    sns.lineplot(
        x=yearly.index,
        y=yearly.values,
        marker="o"
    )

    plt.title("Titles Released by Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")

    st.pyplot(plt)

with col2:

    plt.figure(figsize=(6,4))

    sns.scatterplot(
        data=df,
        x="imdb_score",
        y="tmdb_score"
    )

    plt.title("IMDb vs TMDb Ratings")
    plt.xlabel("IMDb Score")
    plt.ylabel("TMDb Score")

    st.pyplot(plt)

col1, col2 = st.columns(2)

with col1:

    plt.figure(figsize=(6,4))

    sns.countplot(
        data=df,
        y="age_certification",
        order=df["age_certification"].value_counts().index
    )

    plt.title("Age Certification Distribution")
    plt.xlabel("Number of Titles")
    plt.ylabel("Age Certification")

    st.pyplot(plt)  

with col2:

    plt.figure(figsize=(7,5))

    top10 = df.sort_values(
        by="imdb_score",
        ascending=False
    ).head(10)

    sns.barplot(
        data=top10,
        x="imdb_score",
        y="title"
    )

    plt.title("Top 10 Highest IMDb Rated Titles")
    plt.xlabel("IMDb Score")
    plt.ylabel("Title")

    st.pyplot(plt)