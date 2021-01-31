#!/usr/bin/env python3

if __name__ == "__main__":
    from bottle import route, run, static_file
    import os

    @route('/')
    def main():
        return static_file('index.html', root='.')

    with open('index.html', 'wt') as html:
        html.write('My <b>new</b> and <i>improved</i> home page!!')

    print(os.getcwd())
    run(host='localhost', port=9999)

