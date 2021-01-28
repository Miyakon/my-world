#!/usr/bin/env python3

if __name__ == "__main__":
    # SQLiteを使用するなら，ローカルなSQLiteデータベースファイルにconnect()する
    # このファイルはテーブルを保持するデータベースサーバーと同じような役割を果たす．
    # 特殊文字列の':memory:'を指定するとメモリのみにデータベースを作る．
    # これは高速でテスト用には役に立つが，プログラムが終了したりコンピュータが落ちたりすると消える
    import sqlite3
    conn = sqlite3.connect('enterprise.db')  # enterprise.dbへ接続する
    curs = conn.cursor()
    # curs.execute('''CREATE TABLE zoo (critter VERCHAR(20)
    # PRIMARY KEY, count INT, damages FLOAT)''')

    curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
    curs.execute('INSERT INTO zoo VALUES("bear", 3, 10000.0)')

    # データの挿入には，プレースホルダーを使用したより安全な方法がある．
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    print(curs.execute(ins, ('weasel', 1, 20000.0)))

    # データの確認
    curs.execute('SELECT * FROM zoo')
    rows = curs.fetchall()
    print(rows)

    # 同様のデータをソートする
    curs.execute('SELECT * FROM zoo ORDER BY count')

    # 逆順にする
    curs.execute('SELECT * FROM zoo ORDER BY count DESC')

    # 最もダメージが大きい動物はなにか？
    curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')
    curs.fetchall()

    # 終了後にはデータが残らない
