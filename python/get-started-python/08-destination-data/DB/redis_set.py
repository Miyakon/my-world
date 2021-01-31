#!/usr/bin/env python3

if __name__ == "__main__":
    import redis

    conn = redis.Redis('localhost')


    conn.sadd('zoo2', 'duck', 'goat', 'turkey')
    print(conn.scard('zoo2'))
    print(conn.smembers('zoo2'))
    print(conn.srem('zoo2', 'turky'))
