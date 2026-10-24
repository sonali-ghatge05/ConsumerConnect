from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# ---------- Load JSON ----------
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "data", "category_detail.json")

print("Looking for JSON at:", json_path)

try:
    with open(json_path, "r", encoding="utf-8") as file:
        categories_data = json.load(file)
    print("JSON loaded successfully!")
    print("Available categories:", list(categories_data.keys()))
except Exception as e:
    print("Error loading JSON:", e)
    categories_data = {}


# ---------- Routes ----------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/category/<category>")
def category_detail(category):
    print("Requested category:", category)

    category_info = categories_data.get(category)

    if category_info is None:
        return f"Category not found: {category}", 404

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


# ---------- Run App ----------
if __name__ == "__main__":
    app.run(debug=True)