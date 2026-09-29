import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("titles_cleaned.csv")
print(df.head())
print(df.tail())

Content_type= (df["type"].value_counts())
plt.figure(figsize=(6,4))
plt.bar(Content_type.index, Content_type.values)
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(
    Content_type,
    labels=Content_type.index,
    autopct="%1.1f%%"
)
plt.title("Movies vs TV Shows")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["imdb_score"].dropna(),bins=20)
plt.title("imdb_Ratings")
plt.xlabel("Imdb_Score")
plt.ylabel("Frequency")
plt.show()

Released_Year= df["release_year"].value_counts().sort_index()
plt.figure(figsize= (10,5))
plt.plot(Released_Year.index, Released_Year.values)
plt.title("Released Year Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Tiles")
plt.show()

# Highest Rated Movies
Movies= df[df["type"]== "MOVIE"]
Highest_Rated_Movie=Movies.sort_values(by= "imdb_score", ascending= False).head(10)
plt.figure(figsize= (10,6))
plt.bar(Highest_Rated_Movie["title"], Highest_Rated_Movie["imdb_score"])
plt.title("Highest_Rated_Movie")
plt.xlabel("Title")
plt.ylabel("Imdb_Score")
plt.xticks(rotation= 90)
plt.tight_layout()
plt.subplots_adjust(bottom= 0.35)
plt.show()

# Top10 Most Popular Titles;-
Popular_Titles= df.sort_values(by= "tmdb_popularity", ascending= False).head(10)
plt.figure(figsize=(12,6))
plt.bar(Popular_Titles["title"], Popular_Titles["tmdb_popularity"])
plt.title("Top 10 Most Popular Titles")
plt.xlabel("Title")
plt.ylabel("TMDb_Popularity")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Runtime distribution :-
plt.figure(figsize= (8,5))
plt.hist(df["runtime"], bins= 30)
plt.title("Runtime_Distribution")
plt.xlabel("Runtime_Minutes")
plt.ylabel("Frequency")
plt.show()

# Does a higher IMDb rating correspond to higher TMDb popularity?
plt.figure(figsize= (8,5))
plt.scatter(df["imdb_score"], df["tmdb_popularity"])
plt.title("IMDb_Score Vs TMDb_Popularity")
plt.xlabel("IMDb_Score")
plt.ylabel("TMDb_Popularity")
plt.show()

# Top Production Countries ;-
Countries= df["production_countries"].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(Countries.index, Countries.values)
plt.title("Top_Production_Countries")
plt.xlabel("Country")
plt.ylabel("Titles")
plt.xticks(rotation= 90)
plt.tight_layout()
plt.show()

# Are there outliers in runtime
plt.figure(figsize=(5,6))
plt.boxplot(df["runtime"].dropna())
plt.title("Runtime")
plt.show()
