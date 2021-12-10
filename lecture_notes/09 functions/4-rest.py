def f2(*args):
    _type = list(map(type, [*args]))  # similar way: _type = [type(i) for i in [*args]]
    for item, value in enumerate([*args]):
        print(_type[item])
        print(value)  # similar way: print(args[item])
    # similar way for: [print(_type[item],'\n',print(value)) for item, value in enumerate([*args])]
    return


f2(1, 'Marcus', {'field': 'value'})
