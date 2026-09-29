import pandas as pd
df= pd.read_csv("titles_cleaned.csv")
print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

# Which type of content is available more ?
print(df["type"].value_counts())
#Percentage
print(df["type"].value_counts(normalize= True)* 100)

print(df["age_certification"].value_counts())

# Release year with ascending order.
print(df["release_year"].value_counts().sort_index())

print(df["runtime"].mean())
print(round(df["runtime"].mean(),2))  # Number of decimal places.
print(df["runtime"].max())
print(df["runtime"].min())  

print(df["imdb_score"].value_counts())          #Frequency of imdb_score
print(df["imdb_score"].value_counts().mean())   # Avg frequency of unique imdb_score
print(df["imdb_score"].mean())                  # Avg imdb_score

# Which are the top 10 highest-rated movies based on IMDb score?
Highest_score= df.sort_values(by="imdb_score",ascending= False)
print(Highest_score[["title","imdb_score"]].head(10))

# Popular type in tmdb :-
Popular_Title= df.sort_values(by="tmdb_popularity",ascending= False)
print(Popular_Title[["type","tmdb_popularity",]].head(10))

# Highest imdb votes:-
Highest_imdb_votes = df.sort_values(by="imdb_votes", ascending=False)
print(Highest_imdb_votes[["title","imdb_votes"]].head(10))

# Production countries.
print(df["production_countries"].value_counts().head(10))

# Genre Analysis
print(df["genres"].value_counts().head(10))

# Correlation :-
print(df[["runtime",
          "imdb_score",
          "imdb_votes",
          "tmdb_popularity",
          "tmdb_score"]].corr())

# Highest rated movies:-
movies= df[df["type"]== "MOVIE"]
Highest_rated_movies= movies.sort_values(by= "imdb_score", ascending= False)
print(Highest_rated_movies[["title","imdb_score"]].head(10))

# Highest rated show:-
Shows= df[df["type"]== "SHOW"]
Highest_Rated_Show= Shows.sort_values(by= "imdb_score",ascending = False)
print(Highest_Rated_Show[["title","imdb_score"]].head(10))

# Longest Movie
Longest_Movie= df[df["type"]== "MOVIE"]
Longest_Movie_Time= Longest_Movie.sort_values(by= "runtime", ascending= False)
print(Longest_Movie[["title","runtime"]].head(10))