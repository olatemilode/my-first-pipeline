from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, Docker!</h1>"

If __name__ = "__main__":
     app.run(host='0.0.0.0', port=3000)
