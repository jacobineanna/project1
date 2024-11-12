from flask import Flask
import teamc
import teama
import teamb
from hbo_max_routs import init_hbo_max_routes
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!! ??? </p>"

@app.route("/katefelixtrial")
def katefelixtrial():
    return teamc.start()

@app.route("/ayyoubsebastrial")
def ayyoubsebastrial():
    return teama.start()

@app.route("/jacobineniektrial")
def jacobineniektrial():
    return teamb.start()

init_hbo_max_routes(app)
