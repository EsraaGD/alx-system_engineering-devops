#!/usr/bin/python3
"""2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API

    Returns:
        list containing the titles of all hot articles for a given subreddit,
        None if an invalid subreddit is given
    """
    URL = 'https://www.reddit.com/r/'
    res = requests.get('{}{}/hot.json'.format(URL, subreddit),
                       params={'count': count, 'after': after},
                       headers={'User-Agent': 'ALX-User-Agent'},
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    list = hot_list + [child.get('data').get('title')
                       for child in res.json().get('data').get('children')]

    data = res.json()
    if not data.get('data').get('after'):
        return list

    return recurse(subreddit, list, data.get('data').get('count'),
                   data.get('data').get('after'))
