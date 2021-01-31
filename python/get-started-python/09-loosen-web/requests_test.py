#!/usr/bin/env python3

if __name__ == "__main__":
    import requests
    url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    resp = requests.get(url)
    print(resp)
    print(resp.text)