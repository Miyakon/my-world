#!/usr/bin/env python3

class Tiny():
    def __str__(self):
        return 'tiny'

if __name__ == "__main__":
    import pickle
    import datetime

    now1 = datetime.datetime.now()
    pickled = pickle.dumps(now1)
    now2 = pickle.loads(pickled)
    print(now1)
    print(now2)

        
    obj1 = Tiny()
    print('type(obj1)', type(obj1))
    print(obj1)

    # 自作したクラスのインスタンスでもシリアライズできる
    pickled = pickle.dumps(obj1)
    print('pickled =', pickled)
    obj2 = pickle.loads(pickled)
    print(obj2)
