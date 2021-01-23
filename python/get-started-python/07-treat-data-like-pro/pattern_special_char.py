#!/usr/bin/env python3
import string
import re

if __name__ == "__main__":
    printable = string.printable
    print(len(printable))
    print(printable[0:50])
    print(printable[50:])

    print(re.findall(r'\d', printable))
    print(re.findall(r'\w', printable))
    print(re.findall(r'\s', printable))

    x = 'abc' + '-/+' + '\u00ea' + '\u0115'
    print(re.findall(r'\w', x))

    source = '''
    I wish I may, I wish might
    Have a dish of fish tonight.
    '''
    
    print('\n\tGroup A')
    print(source)
    print(re.findall(r'wish', source))
    print(re.findall(r'wish|fish', source))
    print(re.findall(r'^wish', source))
    print(re.findall(r'^I wish', source))
    print(re.findall(r'fish$', source))
    print(re.findall(r'fish tonight.$', source))
    print(re.findall(r'[wf]ish', source))
    print(re.findall(r'[wsh]+', source))  # w, s, hのどれかが１つ以上続いている
    print(re.findall(r'[wsh]*', source))  # 空欄か，w, s, hのどれかが１つ以上続いている

    print('\n\tGroup B')
    print(source)
    print(re.findall(r'ght\W', source))
    print(re.findall(r'I (?=wish)', source))  # Iとスペースの後ろにwishが続く所を探す
    print(re.findall(r'(?<=I) wish', source))  # スペースとwishの前にIがある所を探す
    print(re.findall(r'\bfish', source))  # fishの前が単語の境界
    print(re.findall(r'[^ \s]a', source))  # スペース以外に続くa

    print('\n\tGroup C')
    print(source)
    m = re.search(r'(. dish\b).*(\bfish)', source)
    print(m.group())
    print(m.groups())
    print(m.groupdict())
    m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
    print(m.group())
    print(m.groups())
    print(m.groupdict())
    print(m.group('DISH'))
    print(m.group('FISH'))
    