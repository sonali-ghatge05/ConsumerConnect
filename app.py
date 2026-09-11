from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/category_detail.json", "r", encoding="utf-8") as file:
    categories_data = json.load(file)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/category/<category>")
def category_detail(category):
    category_info = categories_data.get(category)

    if category_info is None:
        return "Category not found", 404

    return render_template(
        "category_detail.html",
        category=category_info
    )


@app.route('/forum-checker')
def forum_checker():
    return render_template('forum_checker.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/About')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)