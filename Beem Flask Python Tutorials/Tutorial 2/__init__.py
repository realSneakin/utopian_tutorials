# Imports
from flask import Flask, render_template, url_for
from steem_data import trending, hot, recent, tag_posts, post_info
import json
import misaka
from flask_misaka import Misaka, Markup, make_flags

# Variables
app = Flask(__name__)
posts_trending = trending
posts_hot = hot
posts_recent = recent
posts_tag = tag_posts

# Functions
def markdown(text, renderer=None, **options):
    ext, rndr = make_flags(**options)
    if renderer:
        md = misaka.Markdown(renderer, ext)
        result = md(text)
    else:
        result = misaka.html(text, extensions=ext, render_flags=rndr)
    if options.get("smartypants"):
        result = misaka.smartypants(result)
    return Markup(result)


# Routes
@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/trending")
def trending():
    trending_posts = posts_trending()
    return render_template("trending.html", trending_posts=trending_posts)


@app.route("/hot")
def hot():
    hot_posts = posts_hot()
    return render_template("hot.html", hot_posts=hot_posts)


@app.route("/recent")
def recent():
    hot_posts = posts_recent()
    return render_template("recent.html", hot_posts=hot_posts)


@app.route("/<section>/<tag>")
def tag_posts(section, tag):
    custom_posts = posts_tag(section, tag)
    return render_template("custom_posts.html", custom_posts=custom_posts)


@app.route("/@<author>/<permalink>")
def blog_post(author, permalink):
    info_post = post_info(author + "/" + permalink)
    json_metadata = json.loads(info_post['json_metadata'])
    return render_template("blog_post.html", post=info_post, json_metadata=json_metadata, markdown=markdown)


# Running The App
if __name__ == "__main__":
    app.run(debug=True)
