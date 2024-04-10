#!/usr/bin/python3
"""1-top_ten module"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API

    Returns:
        titles of the first 10 hot posts listed for a given subreddit,
        None if an invalid subreddit is given
    """
    URL = 'https://www.reddit.com/r/'
    res = requests.get('{}{}/hot.json?limit=10'.format(URL, subreddit),
                       headers={'User-Agent': 'ALX-User-Agent'},
                       allow_redirects=False)

    if res.status_code != 200:
        print('None')

    else:
        [print(child.get('data').get('title'))
         for child in res.json().get('data').get('children')]
