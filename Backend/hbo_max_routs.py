import pandas as pd 
from flask import Flask

def init_hbo_max_routes(app):
    @app.route("/hbo_max_data")
    def hbo_max_data():
        df_hbo = pd.read_csv("HBO_Max.csv")
        print(df_hbo.head(10))

        return 

    @app.route("/hbo_max_IMDB_num_votes")
    def hbo_max_IMDB_votes():
        df_hbo = pd.read_csv("HBO_Max.csv")
        mean_num_votes = df_hbo['imdbNumVotes'].mean()
        median_num_votes = df_hbo['imdbNumVotes'].median()
        std_num_votes = df_hbo['imdbNumVotes'].std()
        return mean_num_votes, median_num_votes, std_num_votes

    @app.route("/hbo_max_IMDB_rating")
    def hbo_max_IMDB_ratings():
        df_hbo = pd.read_csv("HBO_Max.csv")
        mean_rating = df_hbo['imdbAverageRating'].mean()
        median_rating = df_hbo['imdbAverageRating'].median()
        std_rating = df_hbo['imdbAverageRating'].std()
        return mean_rating, median_rating, std_rating

    @app.route("/hbo_max_IMDB_rating_votes")
    def hbo_max_IMDB_rating_votes():
        df = pd.read_csv("HBO_Max.csv")
        df_rating_votes = df["imdbAverageRating", "imdbNumVotes"]

        return df_rating_votes


