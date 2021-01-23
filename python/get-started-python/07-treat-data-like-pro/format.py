#!/usr/bin/env python3

if __name__ == "__main__":
    # old % format
    print('%s' % 42)
    print('%d' % 42)
    print('%x' % 42)
    print('%o' % 42)
    print('%f' % 42)

    print('%s' % 7.03)
    print('%f' % 7.03)
    print('%e' % 7.03)
    print('%g' % 7.03)
    print('%d%%' % 100)

    n = 42
    f = 7.03
    s = 'cheese'
    print('%d, %f, %s' % (n, f, s))
    
    print('\n幅10，右揃え，空白挿入')
    print('%10d, %10f, %10s' % (n, f, s))

    print('\n幅10，左揃え，空白挿入')
    print('%-10d, %-10f, %-10s' % (n, f, s))

    print('\n上限4，右揃え')
    print('%.4d, %.4f, %.4s' % (n, f, s))

    print('\n幅10，上限4，右揃え，空白挿入')
    print('%10.4d, %10.4f, %10.4s' % (n, f, s))

    print('\nフィールド幅と文字列をハードコードせず，引数から指定する')
    print('%*.*d, %*.*f, %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))

    # new {} format