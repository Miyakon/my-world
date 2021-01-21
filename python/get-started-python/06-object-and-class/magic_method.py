#!/usr/bin/env python3

class Word():
    def __init__(self, text: str):
        self.text:str = text

    def __eq__(self, word2: object):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('Ha')
third = Word('eh')

# Magicメソッドにより，記号の意味が確定する．
# すなわち，右辺にあるオブジェクトの__eq__(obj)を呼び出すには
# object_name == obj　と書けばいい
print(first == second)
print(first == third)

class Magic():
    def __init__(self, text):
        self.text = text
    
    def __wq__(self, word2):
        self.text.lower() == word2.text.lower()
    
    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' +  self.text + '")'

mg = Magic('ha')
mg  # インタプリタの場合__repr__を使用する
print(mg)  # __str__を使用する