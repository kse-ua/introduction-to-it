catch_rest = lambda *args: print(args)
catch_rest(1, 2, 3)


def f2(*args):
    for i in args:
        typeOf = str(type(i))
        print('Type:', typeOf)
        print('Value:', i)


f2(1, 'Marcus', { 'field': 'value' })




