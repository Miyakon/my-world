#!/usr/bin/env python3

if __name__ == "__main__":
    # seek()による位置の変更
    fin = open('bfile', 'rb')
    print('tell =', fin.tell())

    print('seek(255) =', fin.seek(255))
    bdata = fin.read()
    print('len(bdata)', len(bdata))
    print(bdata[0])
    fin.seek(0)
    print('fin.seek(-1, 2)', fin.seek(-1, 2))
    bdata = b''
    bdata = fin.read()
    print('len(bdata)', len(bdata))

    print(fin.seek(254, 0))
    print(fin.seek(1, 1))
    print(fin.tell())

    fin.close()

    # seek(offset, origin)の第2引数origin
    # originが
    # 0: 先頭からoffsetの位置へ移動
    # 1: 現在の位置からoffsetバイトの位置へ移動
    # 2: 末尾からoffsetバイトの位置へ移動
    # これらの値は標準のosモジュールでも設定されている
    import os
    print('os.SEEK_SET =', os.SEEK_SET, 
    ', os.SEEK_CUR =', os.SEEK_CUR, 
    ', os.SEEK_END =', os.SEEK_END)
