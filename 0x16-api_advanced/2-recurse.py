#!/usr/bin/python3
"""returns a list containing the titles of all hot
articles for a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """Set the URL for the subreddit's hot posts API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "My User Agent 1.0"}

    # Add the 'after' parameter to the URL if it exists
    if after:
        url += "?after={}".format(after)

    # Query the API and retrieve the response
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code is not OK (200), return None
    if response.status_code != 200:
        return None

    # Parse the JSON response to retrieve the hot posts and their titles
    data = response.json()
    posts = data["data"]["children"]
    titles = [post["data"]["title"] for post in posts]

    # Append the titles to the hot_list
    after = data["data"]["after"]
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list
