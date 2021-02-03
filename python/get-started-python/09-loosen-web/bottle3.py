#!/usr/bin/evn python3

if __name__ == "__main__":
    from bottle import route, run, static_file

    @route('/')
    def home():
        return static_file('index.html', root='.')

    @route('/echo/<thing>')
    def echo(thing):ß
        return "Say hello to my little friend: %s!" % thing

    run(host='localhost', port=9999)


