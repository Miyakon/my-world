#!/usr/bin/env
import pprint

if __name__ == "__main__":
    # byte and byte sequence
    blist = [1, 2, 3, 255]
    print(blist)
    the_bytes = bytes(blist)
    print(f'bytes =  {the_bytes}')
    the_byte_array = bytearray(blist)
    print(f'bytearray = {the_byte_array}')

    the_bytes2 = bytes(range(0, 256))
    the_byte_array2 = bytearray(range(0, 256))

    pprint.pprint(the_bytes2)