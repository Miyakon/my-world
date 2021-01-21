#!/usr/bin/env python3
from collections import namedtuple

import composition

if __name__ == "__main__":
    Duck = namedtuple('Duck', 'bill tail')
    duck = Duck('wide orange', 'long')
    print(duck)
    # Duck(bill='wide orange', tail='long')

    Pract = namedtuple('Pract', 'a b c d e')
    pract = Pract('d', 'e', 'f', 'g', 'h')
    print(pract)
    # Pract(a='d', b='e', c='f', d='g', e='h')

    Name = namedtuple('Na', 'x y z')
    na = Name('a', 'b', 'c')
    print(na)
    # Na(x='a', y='b', z='c')

    duck = composition.Duck('wide orange', 'long')
    print(duck)
    # <composition.Duck object at 0x104063ee0>

    parts = {'bill': 'wide orange', 'tail' : 'long'}
    duck2 = Duck(**parts)
    print(duck2)
    # Duck(bill='wide orange', tail='long')

    # 引数における'**'はキーワード引数．
    # 渡されたイテラブルな値を抽出して引数に渡してくれる

    duck3 = duck2._replace(tail='magnificient', bill='crushing')
    print(duck3.tail)
