def catchRest(*args):
    print(args)

catchRest(1, 2, 3)

def f2 (*args):
    for i1 in args:
        etype = type(i1)
        print(f"Type: {etype}")
        if etype == object:
            i2 = str(i1)
            print(f"Value: {i2}")
        else:
            print(f"Value: {i1}")

f2(1, 'Marcus', { "field" : 'value' })
