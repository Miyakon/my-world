#!/usr/bin/env python3

if __name__ == "__main__":
    settings = """[english]
greeting = Hello

[french]
greeting = Bonjour

[files]
home = /usr/local
# 単純な挿入
bin = %(home)s/bin"""

    with open('settings.cfg', 'wt') as cfgout:
        print(cfgout.write(settings))
    
    import configparser
    cfg = configparser.ConfigParser()
    print('cfg.read(settings.cfg) return', cfg.read('settings.cfg'))
    print('type(cfg) =', type(cfg))
    
    print(cfg['french'])
    print(cfg['french']['greeting'])
    print(cfg['files']['bin'])
    