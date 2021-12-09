def catchRest (*args):
    print(args)

catchRest(2, 4, 5)

def f2 (*args):
    for i in args:
        element_type = type(i)
        print(f"type: {element_type}")
        if element_type == object:
            new_i = str(i)
            print(f"Value: {new_i}")
        else:
            print(f"Value: {i}")
        
f2(1, 'Marcus', {"field": 'value'})
