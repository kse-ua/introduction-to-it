def catchRest (*args):
    print(list(args))
catchRest(2, 4, 5)


def f2 (*args):
    for argument in args:
        argument_type = type(argument)
        print(f"Type: {argument_type}")
        if argument_type == object:
            new_made_string = str(argument)
            print(f"Value: {new_made_string}")
        else:
            print(f"Value: {argument}")

f2(1, 'Marcus', {'field': 'value'})

