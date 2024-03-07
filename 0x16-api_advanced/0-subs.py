#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        int: The number of subscribers for the subreddit.
    """
    # Construct the URL for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define a custom User-Agent to avoid Too Many Requests errors
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Send a GET request to retrieve the subreddit's information
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid, return 0
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "programming"  # Example subreddit
    print(number_of_subscribers(subreddit))
