func catchRest(args: Any...) {
    for val in args {
        print(val)
    }
}

catchRest(args: 1, 2, 3)

func f2(args: Any...) {
    for val in args {
        print("Type: ", type(of: val))
        print("Value:", val)
    }
}

f2(args: 1, "Marcus", "Value")
