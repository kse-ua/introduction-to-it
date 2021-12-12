def add1(first_num, sec_num):
    return first_num + sec_num


def add1(n1, n2):
    res = n1 + n2
    return res

add3 = lambda n1, n2: n1 + n2


print(f" {add1(10, 20)}, {add1(7, 20)}")
print(f" {add3(10, 20)}, {add3(7, 20)}")
