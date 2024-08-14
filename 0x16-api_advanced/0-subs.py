import requests

def number_of_subscribers(subreddit):
    # Base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'my-reddit-script/0.1'}
    
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid or other error occurs, return 0
        return 0
