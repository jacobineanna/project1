import pandas as pd
from json import loads, dumps
from flask import Flask, jsonify

def init_gmet_routes(app):
    @app.route("/gmet_all")
    def gmet_all():
        gmet = pd.read_csv("gmet.csv")

        json_res = gmet.to_json(orient = "records")
        parsed = loads(result)
        print(gmet)
        return dumps(parsed)
    
    @app.route("/gmet_freq")
    def gmet_freq():
        gmet = pd.read_csv("gmet.csv")
        
        mean_freq = gmet["frequency"].mean()

        json_res = {
            'mean_freq': mean_freq
        }

        return json_res


