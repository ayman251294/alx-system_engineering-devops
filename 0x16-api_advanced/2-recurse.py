#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found or if it's an invalid subreddit, it returns None."""

import requests


def recurse(subreddit, after=None):
    """method doc"""
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        next = recurse(subreddit, after)
        all_posts.extend(next)
        return all_posts
    return None
