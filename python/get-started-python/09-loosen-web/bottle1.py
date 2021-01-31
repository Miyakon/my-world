#!/usr/bin/env python3

if __name__ == "__main__":
    from bottle import route, run

    @route('/')
    def home():
        return "It isn't fancy, but it's myhome page"

    run(host='localhost', port=9999)

