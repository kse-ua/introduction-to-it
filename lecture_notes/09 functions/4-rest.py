import json


def catch_rest(*args):
    print(args)


catch_rest(1, 2, 3)


def f2(*args):
    for arg in args:
        types = type(arg)
        print(types)
        if types == "dict":
            print(json.dumps(arg))
        else:
            print(arg)


f2(1, "Marcus", {'field': 'value'})