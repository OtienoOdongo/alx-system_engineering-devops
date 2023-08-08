#!/usr/bin/python3
"""
recursive function that queries and returns
list of titles all hot articles
"""

import requests


def recurse(subreddit, hot_list=None):
    """
    A Recursive function that queries Reddit API
    and returns a list of titles of all hot articles for a given subreddit
    """
    if hot_list is None:
        hot_list = []

    if not is_valid_subreddit(subreddit):
        return []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Google chrome version  115.0.5790.11"}

    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extracting the titles of the hot articles
        articles = data['data']['children']
        for article in articles:
            title = article['data']['title']
            hot_list.append(title)

        # Check if there are more pages to fetch
        after = data['data']['after']
        if after is not None:
            # Recursive call to fetch the next page
            recurse(subreddit, hot_list)

    return hot_list


def is_valid_subreddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Google chrome version  115.0.5790.11"}

    response = requests.get(url, headers=headers)

    # Check if the request was successful and the subreddit exists
    if response.status_code == 200:
        data = response.json()
        if 'error' not in data:
            return True

    return False
