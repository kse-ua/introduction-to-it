def rest(*args):
    print(args)

rest(1, 2, 3)

def f2(*args):
    for element in args:
        element_type = type(element)
        print('Type', element_type)
        if element_type == 'dict':
            print('Value:', str(element))
        else:
            print('Value:', element)

f2(1, 'Marcus', { 'field': 'value' })
