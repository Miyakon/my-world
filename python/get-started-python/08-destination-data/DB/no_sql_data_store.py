#!/usr/bin/env python3

if __name__ == "__main__":
    # dbmファイミリ
    import dbm
    # いつものごとくrは読み出し，wは書き込み，
    # cは．．．読み書き専用で，ファイルがない場合は作成する(この子は初対面だな)
    # dbmopenのファイル名に拡張子は必要ない．気が利くやつなんだ．
    # .dbをつけると.db.dbってしてくれるよ．気が利くからね．
    db = dbm.open('definitions', 'c')
    db['mustard'] = 'yellow'
    db['ketchup'] = 'red'
    db['pesto'] = 'green'

    len(db)
    print(db['pesto'])
    db.close()

    db = dbm.open('definitions', 'r')
    print(db['mustard'])

    # getとsetdefault()が辞書と同じ用に動作することも覚えておこう.