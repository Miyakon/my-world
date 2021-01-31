#!/usr/bin/env python3

if __name__ == "__main__":
    import requests
    url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    resp = requests.get(url)
    print(resp)
    print(resp.text)

    resp = requests.get('http://localhost:9999/echo/Mothra')
    if resp.status_code == 200 and \
        resp.text == 'Say hello to my little friend: Mothra!':
        print('It worked! That alomost never happens!')