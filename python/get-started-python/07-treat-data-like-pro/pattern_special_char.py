#!/usr/bin/env python3
import string
import re

if __name__ == "__main__":
    printable = string.printable
    print(len(printable))
    print(printable[0:50])
    print(printable[50:])

    print(re.findall('\d', printable))
    print(re.findall('\w', printable))
    print(re.findall('\s', printable))

    x = 'abc' + '-/+' + '\u00ea' + '\u0115'
    print(re.findall('\w', x))

