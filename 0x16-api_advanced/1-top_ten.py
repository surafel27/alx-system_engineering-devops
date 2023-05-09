#!/usr/bin/python3
"""queries the Reddit API and prints the titles
   of the first 10 hot posts listed"""


import requests


def top_ten(subreddit):
    """return top_ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit_hot_posts:v1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    posts = data["data"]["children"][:10]
    titles = [post["data"]["title"] for post in posts]
    for title in titles:
        print(title)
