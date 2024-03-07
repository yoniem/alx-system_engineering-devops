#!/usr/bin/python3
"""
Script to recursively retrieve hot posts from a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is None.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Define headers for the HTTP request, including User-Agent
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    
    # Define parameters for the request, including pagination
    params = {"limit": 100, "after": after}
    
    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract relevant data
        data = response.json().get("data")
        after = data.get("after")
        
        # Append post titles to the hot_list
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))
        
        # If there are more posts to retrieve, recursively call the function
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # If the subreddit is invalid or no results are found, return None
        return None

# Example usage
if __name__ == "__main__":
    subreddit = "programming"  # Example subreddit
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
