ages = {}

ages.update({'Vasia Pupkin': 19})
ages.update({'Marcus Aurelius': 1860})
print(f"ages: {ages}")

ages.update({'Vasia Pupkin': 20})
print(f"ages: {ages}")

ages.pop('Vasia Pupkin')
print(f"ages: {ages}")

def check(item):
    return item in ages

print(f"Vasia Pupkin: {check('Vasia Pupkin')},\n Marcus Aurelius: {check('Marcus Aurelius')}")

ages.clear()
print(f"ages: {ages}")
