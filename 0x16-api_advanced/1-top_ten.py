#!/usr/bin/python3
"""
Script to print titles of the first 10 hot posts for a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the titles of the top 10 hottest posts
    results = response.json().get("data")

    for post in results.get("children"):
        print(post.get("data").get("title"))

# Example usage
if __name__ == "__main__":
    subreddit = "programming"  # Example subreddit
    top_ten(subreddit)
