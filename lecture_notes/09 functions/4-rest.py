def catch_rest(*args):
    print(args)
catch_rest(1, 2, 3)
def f2(*args):
    for i in args:
        element_type = type(i)
        print('Type', element_type)
        if element_type == 'dict':
            print('Value:', str(i))
        else:
            print('Value:', i)
f2(1, 'Marcus', { 'field': 'value' })
