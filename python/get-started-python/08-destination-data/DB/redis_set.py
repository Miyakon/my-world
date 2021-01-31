#!/usr/bin/env python3

if __name__ == "__main__":
    import redis

    conn = redis.Redis('localhost')

    # 集合を作成する(集合の追加)
    conn.sadd('zoo2', 'duck', 'goat', 'turkey')

    # 集合の値の数を取得する．
    print(conn.scard('zoo2'))

    # 集合の全ての値を取得する
    print(conn.smembers('zoo2'))

    # 集合から値を取り除く
    print(conn.srem('zoo2', 'turky'))

    # 集合演算を実行するために，もう一つ集合を作る
    conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

    # zoo, better_zooの積集合
    print(conn.sinter('zoo2', 'better_zoo'))

    # zoo2, better_zooの積集合を取得して集合fowl_zooに格納する
    conn.sinterstore('fowl_zoo', 'zoo2', 'better_zoo')

    # 要素取得
    print(conn.smembers('fowl_zoo'))

    # 次は和集合
    conn.sunionstore('fabulous_zoo', 'zoo2', 'better_zoo')

    # 要素取得
    print(conn.smembers('fabulous_zoo'))

    # zoo2にあってbetter_zooにないものは何か
    # sdiff()を使って差集合を取得し，sdiffstore()を使って差集合をzoo_sale集合に格納する
    conn.sdiff('zoo2', 'better_zoo')
    conn.sdiffstore('zoo_sale', 'zoo2', 'better_zoo')
    print(conn.smembers('zoo_sale'))
