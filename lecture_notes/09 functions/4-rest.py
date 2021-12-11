def catch_rest(*args):
    print(args)

catch_rest(1, 2, 3)


def check_type(*args):
    for arg in args:
        type_of = type(arg)
        print('Type: ' + str(type_of) + '\n' + 'Value: ' + str(arg))

check_type(1, 'Marcus', { 'field': 'value' })
