def catch_rest(*args):
    print(list(args))


catch_rest(1, 2, 3)


def f2(*args):
    for argument in args:
        arg_type = type(argument)
        print(f"Type: {arg_type}")
        print(f"Value: {argument}")


f2(1, 'Marcus', {'field': 'value'})
