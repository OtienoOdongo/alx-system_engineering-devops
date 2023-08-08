#!/usr/bin/python3

import request


def number_of_subscribers(subreddit):
    """
    Return total number_of_subscribers of a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        return data['data']['subscribers']
    else:
        return 0
