# Imports
from flask import Flask, render_template, url_for
from steem_data import trending

# Variables
app = Flask(__name__)
posts_trending = trending

# Routes
@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/trending")
def trending():
    trending_posts = posts_trending()
    return render_template("trending.html", trending_posts=trending_posts)


# Running The App
if __name__ == "__main__":
    app.run(debug=True)
