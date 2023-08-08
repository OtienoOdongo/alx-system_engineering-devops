#!/usr/bin/python3
"""
using Reddit API to query and print
first 10 hot posts in agiven subreddit
"""

import requests


def top_ten(subreddit):
    """
    A function that queries and prints titles of the first
    top 10 hot posts in a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Google chrome version  115.0.5790.11"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print("None")
