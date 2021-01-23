#!/usr/bin/env python3

if __name__ == "__main__":
    snowman = '\u2603'
    print(snowman)
    ds = snowman.encode('utf-8')
    print(ds)
    print(len(ds))
    ds_ignore = snowman.encode('ascii', 'ignore')
    ds_replace = snowman.encode('ascii', 'replace')
    print(f'ignore = {ds_ignore}, replace = {ds_replace}')
    # byte文字列のため＋演算子が使えない -> 文字列結合ができない
    # print('ignore = ' + ds_ignore + ', replace = ' + ds_replace)
    print('ignore = %s, replace = %s' % (ds_ignore, ds_replace))