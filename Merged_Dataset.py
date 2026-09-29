import pandas as pd

df= pd.read_csv("Netflix_Merged.csv")

# 1 Shows how Netflix content production changed over time.
yearly_titles=(df[["release_year", "title"]]
               .drop_duplicates()
               .groupby("release_year")
               .size()
               .sort_index()
)
print(yearly_titles) 

# 2 Know how many Movies and TV Shows Netflix has.
types= (
    df[["title","type"]]
    .drop_duplicates()
    .groupby("type")
    .size()
)
print("types")

# 3 top 10 genres
genres= df["genres"].value_counts().sort_values(ascending=False).head(10)
print(genres)

# 4 Top 10 production countries
Production_Country=( 
            df[["title","production_countries"]]
            .groupby("production_countries")
            .size()
            .sort_values(ascending=False)
            .head(10)
)            
print(Production_Country)

# 5 Which are the Top 10 Age Certifications available on Netflix?
Age_Certification= (
    df["age_certification"]
    .value_counts()
    .sort_values(ascending=False)
)
print(Age_Certification)

# 6 Which 10 directors have directed the highest number of Netflix titles?
Directors=(
    df[df["role"] == "DIRECTOR"] ["name"]
    .value_counts()
    .sort_values(ascending= False)
    .head(10)
)
print(Directors)

# 7  Which 10 actors appear in the highest number of Netflix titles?
Actors=(
    df[df["role"]=="ACTOR"]["name"]
    .value_counts()
    .sort_values(ascending= False)
    .head(10)
)
print(Actors)

# 8 Which 10 titles have received the highest IMDb scores?
Highest_IMDb_Score= (
    df[["title","imdb_score"]]
    .sort_values(by="imdb_score", ascending= False)
    .head(10)
)
print(Highest_IMDb_Score)

# 9 Which 10 titles have the longest runtime?
Titles_Runtime= (
    df[["title","runtime"]]
    .sort_values(by ="runtime", ascending= False)
    .head(10)
)
print(Titles_Runtime)

# 10 Which genres have the highest average runtime?
Genre_Runtime= (
    df[["genres", "runtime"]]
    .groupby("genres")
    .mean()
    .sort_values(by= "runtime", ascending= False)
    .head(10)
)
print(Genre_Runtime)
