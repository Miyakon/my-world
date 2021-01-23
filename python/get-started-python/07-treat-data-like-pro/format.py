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
    mystring = '{} {} {}'.format(n, f, s)
    print(mystring)
    string1 = '{2} {0} {1}'.format(f, s, n)
    print(string1)
    string2 = '{n} {f} {s}'.format(n=n, f=f, s=s)
    print(string2)
    string3 = '{0[n]} {0[f]} {0[s]} {1}'.format({'n': n, 'f': f, 's': s}, 'other')
    print(string3)

    print('\n位置引数とともに型指定子を使う')
    print('{0:d} {1:f} {2:s}'.format(n, f, s))

    print('\nキーワード引数とともに型指定子を使う')
    print('{n:d} {f:f} {s:s}'.format(n=n, f=f, s=s))

    print('\nフィールド幅の下限を10として，デフォルトの右揃え')
    print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))  # 文字列に関してはデフォルトで左揃えっぽい
    print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))
    
    print('\nフィールド幅の下限を10として，左揃え')
    print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

    print('\nフィールド幅の下限10として，中央揃え')
    print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

    print('\n上限を4にする-整数では使えない')
    print('{0:010d} {1:10.4f} {2:10.4s}'.format(n, f, s))

    print('\nパディング')
    print('{0:!^20s}'.format('BIG SALE'))