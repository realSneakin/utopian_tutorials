from beem.discussions import Query, Discussions_by_trending, Discussions_by_hot, Discussions_by_created
from beem.account import Account


def tag_posts(section, post_tag):
    posts = []
    if section == "trending":
        tag_query = Query(limit=10, tag=post_tag)
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
    elif section == "recent":
        tag_query = Query(limit=10, tag=post_tag)
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
    elif section == "hot":
        tag_query = Query(limit=10, tag=post_tag)
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
    else:
        posts += [{
            "title": "Wrong Request"
        }]
