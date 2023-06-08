#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

