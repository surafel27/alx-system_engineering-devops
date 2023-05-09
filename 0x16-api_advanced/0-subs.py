#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Set the URL for the subreddit's API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "python:subreddit_subscribers:v1"}

    # Query the API and retrieve the response
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code is not OK (200), return 0
    if response.status_code != 200:
        return 0

    # Parse the JSON response to retrieve the number of subscribers
    data = response.json()
    subscribers = data["data"]["subscribers"]

    return subscribers
