import json


def catchrest(*args):
    print(args)


catchrest(1, 2, 3)


def f2(*args):
    for arg in args:
        type_ = type(arg)
        print('Type: ' + str(type_))
        if type_ == 'dict':
            print('Value: ' + json.dumps(arg))
        else:
            print('Value: ' + str(arg))


f2(1, 'Marcus', {'field': 'value'})
