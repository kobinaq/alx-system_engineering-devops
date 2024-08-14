import requests

def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'
    }
    
    # Parameters for pagination
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    try:
        # Make GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Add titles to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Check if there are more posts
            if data['data']['after']:
                # Recursive call with the 'after' parameter
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                # All posts have been collected
                return hot_list
        elif response.status_code == 404:
            # Subreddit not found
            return None
        else:
            # Other error occurred
            return None
    except:
        # Handle any exceptions (e.g., connection errors)
        return None
