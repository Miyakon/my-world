#!/usr/bin/env python3

class Person():
    def __init__(self, name, word):
        self.name = name
        self.word = word

    def who(self):
        return self.name
    
    def say(self):
        return self.word + '.'

class Miyako(Person):
    def say(self):
        return self.name + ':' + self.word

class Goodman():
    def say(self):
        return 'My name is Goodman'

if __name__ == "__main__":
    def who_says(obj):
        print(obj.say())

    person = Person('person', 'saikou')
    miyako = Miyako('miyako', 'saikou')
    goodman = Goodman()

    who_says(person)
    who_says(miyako)
    who_says(goodman)