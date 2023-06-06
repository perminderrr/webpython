from flask import Flask
app = Flask(__name__)
@app.route("/")
def net_com():
    return "netcom!"
