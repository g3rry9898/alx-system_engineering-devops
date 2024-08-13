#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            hot_list.extend([post["data"]["title"] for post in data["data"]["children"]])
            after = data["data"]["after"]
            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                return process_words(hot_list, word_list)
        else:
            return None
    except requests.RequestException:
        return None

def process_words(hot_list, word_list):
    word_count = {}
    for word in word_list:
        word_count[word.lower()] = 0

    for title in hot_list:
        words = title.lower().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1

    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")

# Example usage
count_words("python", ["Python", "JavaScript", "java"])

