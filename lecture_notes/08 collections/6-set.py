ages = set([10, 12, 15, 17, 18, 18, 19, 20])
print(ages)

ages.add(16)
ages.remove(20)
print(ages)


def check_if_true(element):
    if element in ages:
        return True
    else:
        return False


print(check_if_true(10), check_if_true(16), check_if_true(19), check_if_true(20))

ages.clear()
print(ages)
