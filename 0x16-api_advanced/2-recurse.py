#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}  # Adjust limit as needed

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_list.extend([post["data"]["title"] for post in data["data"]["children"]])
            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None

# Example usage
print(recurse("python"))  # Replace "python" with any subreddit name
