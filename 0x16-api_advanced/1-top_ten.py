#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 404:
        print("None")
        return

    # Retrieve the JSON data from the response
    results = response.json().get("data")

    # Print the titles of the 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
