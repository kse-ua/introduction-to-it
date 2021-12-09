catchRest = lambda *args: print(args)
catchRest(1, 2, 3)


class field:
    def __init__(self, field):
        self.field = field
    
    def __str__(self) -> str:
        return f"'{self.field}'"
    

def f2(*args):
    for arg in args:
        type_of = type(arg).__name__
        print('Type:', type_of)
        print('Value:', arg)




f2(1, 'Marcus', field("value"))

