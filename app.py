from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    return "Categories page coming soon"


@app.route("/forum-checker")
def forum_checker():
    return "Forum Checker coming soon"


@app.route("/resources")
def resources():
    return "Resources page coming soon"


@app.route("/faq")
def faq():
    return "FAQ page coming soon"


if __name__ == "__main__":
    app.run(debug=True)