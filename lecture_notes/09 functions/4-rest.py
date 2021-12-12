def catch_rest(*args):
    print(list(args))


catch_rest(1, 2, 3)


def f2(*args):
    for arg in args:
        print("Type:", type(arg))
        print("Value:", arg)
        print()


f2(1, "Marcus", {"field": "value"})