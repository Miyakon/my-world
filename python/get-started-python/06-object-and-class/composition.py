#!/usr/bin/env python3

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    
    def about(self):
        print('This duck has a', self.bill.description, 'bill and ', self.tail.length, 'tail')
    
if __name__ == "__main__":
    bill = Bill('wide orange')
    tail = Tail('long')
    duck = Duck(bill, tail)
    duck.about()