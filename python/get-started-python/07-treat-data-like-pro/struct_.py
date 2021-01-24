#!/usr/bin/env python3

if __name__ == "__main__":
    import struct

    valid_png_header = b'\x89PNG\r\n\x1a\n'
    data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
        b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

    if data[:8] == valid_png_header:
        width, height = struct.unpack('>LL', data[16:24])
        print('Valid PNG, width', width, 'height', height)
    else:
        print('Not a valid PNG')

    # Pythonデータをバイトに変換する
    print('\n')
    print('>L -> ' + repr(struct.pack('>L', 154)))
    print('<L -> ' + repr(struct.pack('<L', 154)))
    print('>LL -> ' + repr(struct.pack('>LL', 1, 2)))
    