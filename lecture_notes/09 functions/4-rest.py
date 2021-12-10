catchRest = lambda *args: print(args)
catchRest(1, 2, 3)


def f2(*args):
    for arg in args:
        type_of = type(arg)
        print('Type:', type_of)
        print('Value:', arg)


f2(1, 'Marcus', {'field' : 'value'})
