#!/usr/bin/env python3

if __name__ == "__main__":
    # Redisのデータ型でも特に応用範囲が広いのはソート済み集合あるいはzsetと呼ばれるものだ
    # zsetは一意な値の集合だが，それぞれ値がスコアと呼ばれる浮動小数点数を持っている．
    # 要素には値とスコアのどちらからでもアクセス可能だ．
    # zsetにはスコアボード，副インデックス，タイムライン(timestampをスコアとして使う)

    import time
    import redis

    now = time.time()
    print(now)

    conn = redis.Redis()

    # 神経質そうな最初のゲストを追加しよう
    conn.zadd('logins', {'smeagol': now})

    # 5分後に別のゲストがやってくる
    conn.zadd('logins', {'sauron': now+(5*60)})

    # 2時間後に別のゲスト
    conn.zadd('logins', {'bilbo': now+(2*60*60)})

    # 1日後にゆっくりと次のゲスト
    conn.zadd('logins', {'treebeard': now+(24*60*60)})

    # bilboがやってきたのは何番目か
    print('conn.zrank', conn.zrank('logins', 'bilbo'))
    print('conn.zscore', conn.zscore('logins', 'bilbo'))

    # 全員をログイン順で見る
    print('conn.zrange', conn.zrange('logins', 0, -1, withscores=True))


