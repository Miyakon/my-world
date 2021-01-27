#!/usr/bin/env python3

if __name__ == "__main__":

    menu = {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch" : {
            "hours": "11-3",
            "items": {
                "hamburger": "5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

    import json
    import pprint

    # menuはdictのデータ構造であり，json.dumpsで文字列にエンコードされる．
    menu_json = json.dumps(menu)
    print(type(menu_json))

    # 再度Pythonデータ構造に戻す.
    menu2 = json.loads(menu_json)
    print(type(menu2))

    # datetimeなどの1部のオブジェクトはエンコード，デコードで例外を起こすことがある
    import datetime
    now = datetime.datetime.utcnow()
    print(now)
    try:
        json.dumps(now)
    except TypeError:
        print('Occurred "TypeError')
    
    # JSON標準が日付，時刻型を定義していないからである．
    # 処理方法は自分で定義してくれということだ．
    # datetimeを文字列やUnix時間にすればJSONは理解できる
    now_str = str(now)
    print(json.dumps(now_str))
    
    from time import mktime
    now_epock = int(mktime(now.timetuple()))
    print(json.dumps(now_epock))

    # JSONのエンコード方式は継承によって変更できる．
    # PythonのJSONについてのドキュメントには，複素数を対象とした例が掲載されている．
    # これをdatetime用に書き換える
    class DTEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return int(mktime(obj.timetuple()))
            return super.default(self, obj)

    # DTEncoderはJSONEncorderのサブクラスである．
    # datetime処理は，default()メソッドをオーバーライドするだけで追加できる．



    # 継承のおかげで．他のすべての処理は親クラスで実行される．
    # isinstance()関数は，objが引数のクラスのオブジェクトかをチェックする
    print('type(now)=', type(now))
    