#!/usr/bin/env python3

if __name__ == "__main__":
    import memcache
    db = memcache.Client(['127.0.0.1:11211'])
    print(db.set('marco', 'polo'))
    print(db.set('duck', 0))

    print(db.get('marco'))
    print(db.get('duck'))
