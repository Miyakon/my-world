#!/bin/usr/env python3

if __name__ == "__main__":
    mcintyre = """name:
    first: James
    last: McIntyre
dates:
    birth: 1828-05-25
    death: 1096-03-31
details:
    bearded: true
    themes: [cheese, Canada]
books:
    url: http://www.gutenberg.org/files/36068/36068-h/36068-h.htm
poems:
    - title: 'Canadian Charms'
      text: |
        Here industry is not in vain,
        For we have bounteous crops ofgrain,
        And you behold on every field
        Of grass and roots abundant yield,
        But after all the greatest charm
        Is the snug home upon the farm,
        And stone walls now keep cattle warm.
    - title: 'Motto'
      text: |
        Politeness, Perseverance and pluck,
        To their possessor will bring good luck.
flags:
    one: on
    two: off
    """

    with open('mcintyre.yaml', 'wt') as yamlout:
        yamlout.write(mcintyre)

    # true, false, on, offなどの値は，Pythonのブール値に変換される．
    # 整数と文字列はそれぞれPythonの整数と文字列に変換される．
    # その他の構文は，リストまたは辞書になる．

    import yaml
    with open('mcintyre.yaml', 'rt') as fin:
        text = fin.read()
        print(text)  #  plain text
    
    data = yaml.load(text)
    print('type(data) =', type(data))
    print(data['poems'][0]['text'])
    print(data['flags']['one'])
    print(data['flags']['two'])
    