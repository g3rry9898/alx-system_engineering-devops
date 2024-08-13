#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)

# Example usage
top_ten("python")  # Replace "python" with any subreddit name

