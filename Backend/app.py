from flask import Flask
from flask import render_template
import teamc
import teama
import teamb
from hbo_max_routs import init_hbo_max_routes

app = Flask(__name__)

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
