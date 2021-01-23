#!/usr/bin/env python3

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)

    print('value = "%s", name = "%s", value2 = "%s"' % (value, name, value2))

if __name__ == "__main__":
    unicode_test('a')
    unicode_test('$')
    unicode_test('\u00a2')
    unicode_test('\u20ac')
    unicode_test('\u2603')

    import unicodedata
    print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))
    
    place = 'caf\u00e9'
    print(place) 
    # place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
    place = 'caf\N{latin small letter e with acute}'
    
    print(place)
