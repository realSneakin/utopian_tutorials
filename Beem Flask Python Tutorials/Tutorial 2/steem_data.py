# Imports
from beem.discussions import Query, Discussions_by_trending, Discussions_by_hot, Discussions_by_created
from beem.account import Account
from beem.comment import Comment

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


def hot():
    posts = []
    for post in Discussions_by_hot(query):
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


def recent():
    posts = []
    for post in Discussions_by_created(query):
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


def tag_posts(section, tag):
    posts = []
    if section == "trending":
        tag_query = Query(limit=10, tag=tag)
        for post in Discussions_by_trending(tag_query):
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
    elif section == "recent":
        tag_query = Query(limit=10, tag=tag)
        for post in Discussions_by_created(tag_query):
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
    elif section == "hot":
        tag_query = Query(limit=10, tag=tag)
        for post in Discussions_by_hot(tag_query):
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
    else:
        posts += [{
            "title": "Wrong Request"
        }]
        return posts

def post_info(permalink):
    post = Comment(permalink)
    p_export = post.json()
    return p_export
