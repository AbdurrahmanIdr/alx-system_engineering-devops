#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves all hot articles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles (default=[]).
        after (str): Token for pagination, indicating the starting point (default="").
        count (int): Number of articles already retrieved (default=0).

    Returns:
        list: List containing the titles of all hot articles.
              Returns None if the subreddit is not valid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # Recursively call the function if there are more articles to retrieve
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list

