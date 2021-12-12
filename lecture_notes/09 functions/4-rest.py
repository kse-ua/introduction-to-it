import json

def catchRest(*args):
   print(args)

catchRest(1, 2, 3)


def f2(*args):
    for arg in args:
        type_arg = type(arg)
        print('Type: ', type_arg)
        if type == dict:
            print('Value: ', json.dumps(arg))
        else:
            print('Value: ', arg)

f2(1, 'Marcus', { 6: 'value' })
