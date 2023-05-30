
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/test")
def hello_test():
    return "Welcome to testing!"
if __name__ == "__main__":
    app.run()

