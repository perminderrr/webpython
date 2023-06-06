from flask import Flask
app = Flask(__name__)
@app.route("/")
def met_com():
    return "met com!"

