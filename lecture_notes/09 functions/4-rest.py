def catch_rest(*args):
    print(args)

catch_rest(1, 2, 3)

def f2(*args):
    for arg in args:
        type_of = type(arg)
        print("Type:", type_of)
        if type_of is dict:
            print("Value:", str(arg))
        else:
            print("Value:", arg)
    return


f2(1, "Marcus", { 13: "value" })
