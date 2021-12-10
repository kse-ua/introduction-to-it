def catchRest(*args):
    print(args)
    
def f2(*args):
    for arg in args:
        print(type(arg))
        print(arg)

catchRest(1,2,3)
f2(1, 'Marcus', { "field": 'value' })
