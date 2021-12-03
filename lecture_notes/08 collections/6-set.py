ages = set([10, 12, 15, 17, 18, 18, 19, 20])
print(ages)

ages.add(9)
ages.remove(20)


def check_if_true(number):
    if number in ages:
        return True
    else:
        return False

print(ages)
