#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    """
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    if after is None:
        word_list = [word.lower() for word in word_list]

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]
        after = data["after"]
        children = data["children"]
        for child in children:
            title = child["data"]["title"].lower()
            for word in title.split(" "):
                if word in word_list:
                    found_list.append(word)

        if after is not None:
            count_words(subreddit, word_list, found_list, after)
        else:
            word_count = {}
            for word in found_list:
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    else:
        return
