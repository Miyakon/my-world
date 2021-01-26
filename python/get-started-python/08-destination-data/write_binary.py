#!/bin/usr/env python3

if __name__ == "__main__":
    # binaryの0から5までの256バイトを生成する
    data = bytes(range(0, 256))
    print(len(data))
    print(data)

    fout = open('bfile', 'wb')
    bsize = fout.write(data)
    fout.close()
    print(bsize)

    fout = open('bfile', 'wb')
    size = len(data)
    offset = 0
    chunk = 100

    while(True):
        if offset > size:
            break
        fout.write(data[offset: offset+chunk])
        offset += chunk

    poem: str = '''There was a young lady named Bright,
    Whose speed was far faster than light;
    She started one day
    In a relative way.
    And returned on the previous night.'''

    with open('relativily', 'wt') as fout:
        print(fout.write(poem))
