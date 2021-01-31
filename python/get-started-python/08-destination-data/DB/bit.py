#!/usr/bin/env python3

if __name__ == "__main__":
    import redis

    conn = redis.Redis()

    days = ['2013-02-25', '2013-02-26','2013-02-27']
    big_spender = 1089
    tire_kicker = 40459
    late_joiner = 550212

    conn.setbit(days[0], big_spender, 1)
    conn.setbit(days[0], tire_kicker, 1)
    conn.setbit(days[1], big_spender, 1)
    conn.setbit(days[2], big_spender, 1)
    conn.setbit(days[2], late_joiner, 1)

    # この3日間の各日の訪問者数を調べる
    for day in days:
        print(conn.bitcount(day))

    # 特定の日に特定のユーザが来ているかどうかも調べられる
    print(conn.getbit(days[1], tire_kicker))

    # 毎日ログインしてきたユーザは何人いるか
    print(conn.bitop('and', 'everyday', *days))
    print(conn.bitcount('everyday'))

    # それは誰だったか(valueからkeyを探す)
    print(conn.getbit('everyday', big_spender))

    # この3日間のユニークユーザの合計は何人になるか．
    conn.bitop('or', 'alldays', *days)
    conn.bitcount('alldays')

    # キャッシュと有効期限 expire()
    import time

    key = 'now you see it'
    conn.set(key, 'but not for long')
    conn.expire(key, 5)
    print(conn.ttl(key), conn.get(key))
    time.sleep(6)
    print(conn.ttl(key), conn.get(key))


