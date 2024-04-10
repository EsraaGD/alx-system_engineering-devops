#!/usr/bin/python3
"""100-count module"""
import requests


def count_words(subreddit, word_list=[], word_count={}, after=None):
    """
    Queries the Reddit API recursively

    Returns:
        Prints a sorted count of given keywords
        None if an invalid subreddit is given
    """
    URL = 'https://www.reddit.com/r/'
    res = requests.get('{}{}/hot.json'.
                       format(URL, subreddit),
                       params={'after': after},
                       headers={'User-Agent': 'ALX-User-Agent'},
                       allow_redirects=False)

    if res.status_code >= 300:
        return None

    list = hot_list + [child.get('data').get('title')
                       for child in res.json().get('data').get('children')]

    data = res.json()
    if not data.get('data').get('after'):
        return list

    return recurse(subreddit, list, data.get('data').get('count'),
                   data.get('data').get('after'))
