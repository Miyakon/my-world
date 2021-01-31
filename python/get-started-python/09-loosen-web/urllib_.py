#!/usr/bin/env python3

if __name__ == "__main__":
    import urllib.request as ur
    url = 'https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/fortune_cookie_random1.txt'
    conn = ur.urlopen(url)
    print(conn)

    # 公式ドキュメントによれば， connはいくつかのメソッドをもつHTTPResponseオブジェクトだとされている．
    # read()メソッドは，ウェブページからのデータを与えてくれる

    data = conn.read()
    print(data)

    print(conn.status)

    for key, value in conn.getheaders():
        print(key, value)