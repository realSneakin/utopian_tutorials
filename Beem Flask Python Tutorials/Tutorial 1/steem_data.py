# Imports
from beem.discussions import Query, Discussions_by_trending
from beem.account import Account


# Variables
query = Query(limit=10)

# Functions
def trending():
    posts = []
    for post in Discussions_by_trending(query):
        if "image" in post.json_metadata:
            picture = post.json_metadata["image"]
            acc = Account(post["author"])
            rep = acc.rep
            posts += [{
                "title": post["title"],
                "content": post.body,
                "author": post["author"],
                "author_rep": rep,
                "image": picture[0],
                "permalink": post["permlink"]
            }]
        else:
            acc = Account(post["author"])
            rep = acc.rep
            posts += [{
                "title": post["title"],
                "content": post.body,
                "author": post["author"],
                "author_rep": rep,
                "permalink": post["permlink"]
            }]
    return posts