catchRest = lambda *args: print(*args)

catchRest(1, 2, 3)

def f2(*args):
    for arg in args:
        print('Type: ', type(arg))
        print('Value: ', arg)


f2(1, 'Marcus', 'value')