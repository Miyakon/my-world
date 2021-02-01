L = [1,2,3]
print(*L)

def test(abc, **D):
    print(D)

D = {
    'k1': 'v1',
    'k2': 'v2'
}

print(D)
test(abc="a", d='d', e='e')