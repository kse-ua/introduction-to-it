def catch_rest(*args):
    print(args, '\n')
    
catch_rest(1, 2, 3)

def f2(*args):
    for arg in args:
        type_of_arg = str(type(arg))
        print("Type: " + type_of_arg[7:-1])
        print("Value:", arg, "\n")

f2(1, 'Marcus', { 'field': 'value' })
