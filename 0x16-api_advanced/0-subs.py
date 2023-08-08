#!/usr/bin/python3
"""
A function that queries Reddit API
and returns the total number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return total number_of_subscribers of a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Google chrome version  115.0.5790.11"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        return data['data']['subscribers']
    else:
        if response.status.code == 404:
            return 0
