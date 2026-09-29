import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv("titles_cleaned.csv")

# Movie Vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="type")
plt.title("Movies_Vs_Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Average IMDb Score by Type
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="type", y= "imdb_score")
plt.title("Average_IMDb_Score")
plt.xlabel("Type")
plt.ylabel("IMDb_Score")
plt.show()

# Shows trends over an ordered variable (usually time).
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x= "release_year", y="imdb_score")
plt.title("IMDb_Score_Over_Released_Year")
plt.xlabel("Release Year")
plt.ylabel("IMDb Score")
plt.show()

# IMDb Score Vs TMDb Popularity
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="imdb_score",
    y="tmdb_popularity"
)
plt.title("IMDb Score vs TMDb Popularity")
plt.xlabel("IMDb Score")
plt.ylabel("TMDb Popularity")
plt.show()

# Runtime
plt.figure(figsize=(7,5))
sns.histplot(
    data=df,
    x="runtime",
    bins=20
)
plt.title("Runtime Distribution")
plt.xlabel("Runtime")
plt.ylabel("Frequency")
plt.show()

# IMDb_Score_Distibution
plt.figure(figsize=(7,5))
sns.kdeplot(
    data=df,
    x="imdb_score",
    fill=True
)
plt.title("IMDb Score Distribution")
plt.show()

# Runtime_Distribution
plt.figure(figsize=(6,5))
sns.boxplot(
    data=df,
    y="runtime"
)
plt.title("Runtime Box Plot")
plt.show()

# Runtime_Distribution
plt.figure(figsize=(6,5))
sns.violinplot(
    data=df,
    y="runtime"
)
plt.title("Runtime Distribution")
plt.show()

# IMDb Score by Type
plt.figure(figsize=(6,5))
sns.stripplot(
    data=df,
    x="type",
    y="imdb_score"
)
plt.title("IMDb Score by Type")
plt.show()

# IMDb Score by Type
plt.figure(figsize=(6,5))
sns.swarmplot(
    data=df,
    x="type",
    y="imdb_score",
    size= 2
)
plt.title("IMDb Score by Type")
plt.show()

