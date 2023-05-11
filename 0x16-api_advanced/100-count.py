#!/usr/bin/python3
"""recursive function parses the title of all hot articles,
and prints a sorted count of given keywords"""


import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """takes in a subreddit name and a list of keywords as arguments"""
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        for article in articles:
            title = article['data']['title']
            words = title.lower().split()

            for word in word_list:
                if word.lower() in words:
                    if word.lower() in counts:
                        counts[word.lower()] += 1
                    else:
                        counts[word.lower()] = 1

        after = data['data']['after']

        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or error occurred.")


# Example usage
count_words("python", ["python", "javascript", "java"])
