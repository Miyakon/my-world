#!/usr/bin/env python3

if __name__ == "__main__":
    # readでファイルを読み込む．ファイルサイズ分だけメモリを要求する
    fin = open('relativily', 'rt')
    poem = fin.read()
    fin.close()
    print(len(poem))

    poem = ''
    fin = open('relativily', 'rt')
    chunk = 100
    while True:
        fragment = fin.read(chunk) # すべて読んだ後では' 'の空文字が返され，Falseになる
        print(fragment)
        if not fragment:
            break
        poem += fragment

    fin.close()
    print(len(poem))

    # readlineで1行づつファイルを読み込む
    poem = ''
    fin = open('relativily', 'rt')
    while True:
        line = fin.readline()
        print(line)
        if not line:
            break
        poem += line
    
    fin.close()
    print(len(poem))

    # イテレータでファイルを1行づつ読み込む
    poem = ''
    fin = open('relativily', 'rt')
    for line in fin:
        poem += line
    
    fin.close()
    print(len(poem))

    # readlinesによる1行ごとのリスト取得
    poem = ''
    fin = open('relativily', 'rt')
    lines = fin.readlines()
    fin.close()
    print(len(lines))
    
    for line in lines:
        poem += line 
    
    print(len(poem))
        