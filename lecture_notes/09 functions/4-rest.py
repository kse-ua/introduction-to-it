def catchRest(args):
    print(args)


catchRest([1, 2, 3])


def ObjTypes(args):
    for arg in args:
        print('Type:', type(arg))
        print('Value: ', arg)


args = [1, 'Marcus', {'field': 'value'}]


ObjTypes(args)
