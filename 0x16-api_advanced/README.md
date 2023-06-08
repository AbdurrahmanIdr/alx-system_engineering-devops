## API Advanced Project

This project focuses on practicing API calls using the Reddit API. The provided code allows you to query the Reddit API.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- Requests module
- PEP 8 style
- Executable files

## Installation

1. Install Ubuntu 14.04 LTS on your machine.
2. Install Python 3.4.3.
3. Install the Requests module using `pip install requests`.

## Setup

To use the functions in this project, make sure you have the following prerequisites:

- Python 3.x installed
- The `requests` library installed (you can install it using `pip install requests`)

## Available Functions

### 0. number_of_subscribers

This function queries the Reddit API and returns the number of subscribers for a given subreddit.

#### Prototype

```
def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if the subreddit is invalid.
    """
```

### 1. top_ten
This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

#### Prototype
```
def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
```
### 2. recurse
This recursive function queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

#### Prototype
```
def recurse(subreddit, hot_list=[]):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.

    Returns:
        list: The list of titles of hot articles. Returns None if no results are found or the subreddit is invalid.
    """
```
### 3. count_words
This recursive function queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.

#### Prototype
```
def count_words(subreddit, word_list, found_list=[], after=None):
    """
    Prints a sorted count of given keywords found in the titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.
        found_list (list): A list to store the found keywords.
        after (str): The parameter for the next page of the API results.

    Returns:
        None
    """
```
### Usage
To use the functions, you can import them into your Python script and call them with the required arguments. Here's an example:

```
from reddit_api import number_of_subscribers, top_ten, recurse, count_words

# Get the number of subscribers for a subreddit
subscribers = number_of_subscribers("programming")
print(f"Number of subscribers: {subscribers}")

# Print the titles of the first 10 hot posts for a subreddit
top_ten("programming")

# Get the titles of all hot articles for a subreddit
articles = recurse("programming")
print(articles)

# Print the count of keywords in the titles of hot articles for a subreddit
count_words("programming", ["python", "java", "javascript"])
Make sure to replace "programming" with the name of the desired subreddit and provide valid keyword lists as required.
```
### License
This project is licensed under the ALX SE program License.