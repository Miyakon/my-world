#!/usr/bin/env python3

import os

if __name__ == "__main__":
    poem: str = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a relative way.
    And returned on the previous night.'''

    print(len(poem))

    print(__file__)
    print(os.getcwd())

    cwd = os.getcwd()

    fout = open('./relativily', 'wt')
    r_value = fout.write(poem)
    p_value = print(poem, file=fout)

    print(poem, file=fout, sep=' ', end='\n')

    size = len(poem)
    offset = 0
    chunk = 100
    while True:
        if offset > size:
            break
        print(f'offset = {offset}, chunk = {chunk}')
        w_size = fout.write(poem[offset:offset+chunk])
        offset += chunk
        print(f'write size = {w_size}')

    # Close file stream
    fout.close()

    # mode x によるファイルの上書き禁止
    # このままだとFileExistErrorになる

    try:
        foutx = open('./relativily', 'xt')
        foutx.write('stomp stopm stomp')

        foutx.close()
    except FileExistsError:
        print('relativity already exists!. That was a close one.')
