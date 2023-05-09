#!/usr/bin/python3
"""returns a list containing the titles of all hot
articles for a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Set the URL for the subreddit's hot posts API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url += "?after={}?count={}?limit=100".format(after, count)
    headers = {"User-Agent": "python:subreddit_hot_posts:v1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    titles = [post["data"]["title"] for post in posts]
    hot_list += titles
    after = data["data"]["after"]
    count += data["data"]["dist"]
    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
