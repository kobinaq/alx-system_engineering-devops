#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }
    
    try:
        # Make GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Subreddit not found or other error
            return (0)
    except:
        # Handle any exceptions (e.g., connection errors)
        return (0)
