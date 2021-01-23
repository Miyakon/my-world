#!/usr/bin/env python3

import re

if __name__ == "__main__":

    target = 'Young Frankenstein You'
    result = re.match('You', target)
    print(result)
    print(type(result))

    # 先にパターンをコンパイルして，後で行うマッチングのスピードを上げることができる.
    youpattern = re.compile('You')
    result2 = re.match(youpattern, target)

    # search()は最初のマッチを返す.
    result_search = re.search(youpattern, target)
    print(result_search)

    # findall()は，重なり合わない全てのマッチのリストを返す.
    result_findall = re.findall(youpattern, target)
    print(result_findall)

    # split()は，パターンにマッチしたところでソースを分割し，部分文字列のリストを返す．
    result_split = re.split(youpattern, target)
    print(result_split)

    # sub()は，置換文字列を引数にとり，ソースのうち，パターンにマッチする全ての部分を置換文字列に置き換える
    result_sub = re.sub(youpattern, 'I', target)
    print(result_sub)

    # match()による正確なマッチ
    m = re.match(youpattern, target) # match()は先頭がパターン一致するか見る
    print(m.group())

    m = re.search('Frank', target)
    print(m.group())

    m = re.match('.*Frank', target)
    print(m.group())
