#!/usr/bin/env python3

import redis
conn = redis.Redis()
# 以下と同じ結果が得られる
# redis.Redis('localhost')
# redis.Redis('localhost', 6379)

print('conn.keys()', conn.keys())

conn.set('secret', 'ni!')
conn.set('carats', '24')
conn.set('fever', '101.5')

print('get secret, carats, fever',
conn.get('secret'),
conn.get('carats'),
conn.get('fever'))

print('setnx()はキーが存在しない場合にのみ設定する')
print('setnx(\'secret\', \'hi!\')', conn.setnx('secret', 'hi!'))

print('getset()はもともとの値を取得し，新しい値を設定する')
print('conn.getset(\'secret\', \'icky\')', conn.getset('secret', 'icky'))
print('conn.get(\'secret\')', conn.get('secret'))
print(conn.getrange('secret', -3, -1))
print(conn.setrange('secret', 0, 'X'))
print(conn.get('secret'))

# 複数の値の設定
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
print(conn.mget(['fever', 'carats']))

print('kyes', conn.keys())
conn.delete('cordial')
print('kyes', conn.keys())

print('conn.get(\'carats\')', conn.get('carats'))
conn.incr('carats')
print('conn.get(\'carats\')', conn.get('carats'))
conn.decr('carats')
print('conn.get(\'carats\')', conn.get('carats'))

print('conn.get(\'fever\')', conn.get('fever'))
conn.incrbyfloat('fever')
print('conn.get(\'fever\')', conn.get('fever'))
conn.incrbyfloat('fever', -2.0)
print('conn.get(\'fever\')', conn.get('fever'))

# リスト
# Redisリストは文字列しか格納できない．
# 最初の挿入を行ったときに作成される．先頭への挿入には，lpushを，末尾へはrpushを使う．
conn.lpush('zoo', 'bear')
conn.lpush('zoo', 'alligator', 'duck')
conn.linsert('zoo', 'before', 'bear', 'beaver')
conn.linsert('zoo', 'after', 'bear', 'cassowary')

# lset()で指定した位置に挿入する
conn.lset('zoo', 2, 'marmoset')

conn.rpush('zoo', 'yak')

# 指定のindexの値を取る
print(conn.lrange('zoo', 0, -1))
print(conn.lindex('zoo', 3))
print(conn.lrange('zoo', 0, 2))

