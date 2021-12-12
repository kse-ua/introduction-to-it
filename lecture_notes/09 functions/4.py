import json


def catch_rest(*args)
    print(args)


catch_rest(1, 2, 3)


def f2(*args):
    for arg in args:
        arg_type = type(arg)
        print("Type: ", arg_type)
        if isinstance (arg_type, object):
            print("Value: ", json.dumps(arg))
        else:
            print("Value: ", arg_type)


f2(1, "Marcus", {"field": "value"})