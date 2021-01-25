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

    fout = open('./relatively', 'wt')
    # r_value = fout.write(poem)
    p_value = print(poem, file=fout)

    print(poem, file=fout, sep=' ', end='\n')
    fout.close()