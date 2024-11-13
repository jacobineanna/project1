import pandas as pd
from json import loads, dumps
from flask import Flask, jsonify
from utils.connector import connection

db_connection = connection()


def init_hbo_max_routes(app):
    @app.route("/init_hbo_db")
    def init_hbo_db():
        connection()
        return 'dit werkt'


    @app.route("/hbo_max_data")
    def hbo_max_data():
        df_hbo = pd.read_csv("HBO_Max.csv")
        
        json_res = df_hbo.to_json()
        parsed = loads(json_res)
        return parsed

    @app.route("/hbo_max_IMDB_num_votes")
    def hbo_max_IMDB_votes():
        df_hbo = pd.read_csv("HBO_Max.csv")
        mean_num_votes = df_hbo['imdbNumVotes'].mean()
        median_num_votes = df_hbo['imdbNumVotes'].median()
        std_num_votes = df_hbo['imdbNumVotes'].std()

        json_res = {
            'mean_num_votes': mean_num_votes,
            'median_num_votes': median_num_votes,
            'std_num_votes': std_num_votes
        }

        return json_res

    @app.route("/hbo_max_IMDB_rating")
    def hbo_max_IMDB_ratings():
        df_hbo = pd.read_csv("HBO_Max.csv")
        mean_rating = df_hbo['imdbAverageRating'].mean()
        median_rating = df_hbo['imdbAverageRating'].median()
        std_rating = df_hbo['imdbAverageRating'].std()

        json_res = {
            'mean_average_rating' : mean_average_rating,
            'median_average_rating' : median_average_rating,
            'std_averagre_rating' : std_averagre_rating
        }

        return json_res

    @app.route("/hbo_max_IMDB_rating_votes")
    def hbo_max_IMDB_rating_votes():
        df = pd.read_csv("HBO_Max.csv")
        df_rating_votes = df[["imdbAverageRating", "imdbNumVotes"]]

        # only take the columns where the value's are not NAN
        df_rating_votes = df_rating_votes[df_rating_votes["imdbAverageRating"].notna() & df_rating_votes["imdbNumVotes"].notna()]

        json_res = df_rating_votes.to_json(orient="columns")

        return jsonify(json_res)
    
    @app.route("/hbo_db_get_all")
    def hbo_db_get_all():
        res = db_connection.get_all()
        return jsonify(res)
