from pprint import pprint

def catchRest(*args):
    print(list(args))

catchRest(1,2,3)

def f2(*args):
    for arg in args:
        arg_type = type(arg)
        print("Type:", arg_type)

        if arg_type is dict:
            print("Value: ", end="")
            print(arg)
        else:
            print("Value:", arg)

f2(1, "Marcus", {"field" : "value"})
