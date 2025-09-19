from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask!"


@app.route("/hello")
def hello():
    return "Hello World! HelloFlask!"


if __name__ == "__main__":
    app.run(debug=True)
