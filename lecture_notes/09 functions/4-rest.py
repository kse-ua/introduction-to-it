def catch_rest(*args):
    print(args)

catch_rest(1, 2, 3)

def f2(*args):
    for arg in args:
        print("type:", type(arg))
        print("Value:", arg)


f2(1, 'Marcus', {'field': 'value'})
