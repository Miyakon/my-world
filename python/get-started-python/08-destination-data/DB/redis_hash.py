#!/usr/bin/env python3

if __name__ == "__main__":
    import redis

    # Redis のハッシュは，Pythonの辞書とよく似ているが，文字列しか格納できない．
    # 深さは1レベルだけに限られ，深くネストされた構造は作れない．
    # songというRedisハッシュを作って操作する
    conn = redis.Redis('localhost')
    conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})

    # hset()を使ってハッシュ内の1個のフィールドの値を設定する．
    conn.hset('song', 'mi', 'a note to follow re')

    # hget()を使って1個のフィールドの値を取得する
    print(conn.hget('song', 'mi'))

    # hmget()を使って複数のフィールドの値を取得する
    print(conn.hmget('song', 're', 'do'))

    # hkeys()を使ってハッシュの全てのフィールドのキーを取得する
    print(conn.hkeys('song'))

    # hlen()を使ってハッシュのフィールド数を取得する
    print(conn.hlen('song'))

    # hgetall()を使ってハッシュの全てのフィールドのキーと値を取得する
    print(conn.hgetall('song'))

    # hsetnx()でキーがまだ無ければフィールドを設定する
    print(conn.hsetnx('song', 'mi', 'hello'))
