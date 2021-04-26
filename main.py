from flask import Flask, redirect, url_for, render_template
from githubapi import *

repos = load_repos()

app = Flask(__name__)
app.secret_key = "hello"


@app.route("/")
def main():
    return render_template("index.html", repos=repos)


if __name__ == "__main__":
    app.run(debug=True)