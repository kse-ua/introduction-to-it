def display(*args):
    print(args)


display(1, 2, 3)


def type_of_args(*args):
    for arg in args:
        arg_type = type(arg)
        print('Type: ', arg_type)
        if arg == 'dict':
            print('Value:', str(arg))
        else:
            print('Value:', arg)


type_of_args(1, 'Marcus', {"field": 'value'})
