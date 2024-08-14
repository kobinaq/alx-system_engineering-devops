import requests

def top_ten(subreddit):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
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
            posts = data['data']['children']
            
            for post in posts:
                print(post['data']['title'])
        else:
            # Subreddit not found or other error
            print(None)
    except:
        # Handle any exceptions (e.g., connection errors)
        print(None)
