from flask import Flask
import teamc
import teama
import teamb


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
