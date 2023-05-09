#!/usr/bin/python3
"""returns a list containing the titles of all hot
articles for a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Set the URL for the subreddit's hot posts API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    if after:
        url += "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    titles = [post["data"]["title"] for post in posts]
    after = data["data"]["after"]
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list
