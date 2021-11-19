import sys

var = sys.argv[1]

def loop_func(var):
    print("Begin")
    for i in range(0, int(var), 1):
        print("i: ", i)
    print("end")

loop_func(var)
