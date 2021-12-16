import json


def catch_rest(*args):
    print(*args)


catch_rest(1, 2, 3)


def f2(*args):
    def process_argument(arg):
        arg_type = type(arg)
        print(f'Type: {arg_type.__name__}')

        if arg_type is dict:
            print('Value:', json.dumps(arg))
        else:
            print(f'Value: {arg}')

    list(map(process_argument, args))


f2(1, 'Marcus', {'field': 'value'})
