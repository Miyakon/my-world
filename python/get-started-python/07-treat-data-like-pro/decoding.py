#!/usr/bin/env

if __name__ == "__main__":
    place = 'caf\u00e9'
    print(place)
    # reprを使うことで出力を文字列に変換して，'+'演算子を使用できる.
    print('place type = ' + repr(type(place)))

    place_bytes = place.encode('utf-8')
    print(place_bytes)
    print('place_bytes type = ' + repr(type(place_bytes)))
    print(len(place_bytes))

    place2 = place_bytes.decode('utf-8')
    print(f'place2 = {place2}')
    