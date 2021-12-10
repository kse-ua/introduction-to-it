cities = ["Athens", "Rome", "London", "Beijing", "Kiev", "Riga"]
def f(s):
    return len(s)

def f1():
    cities = ["Athens", "Rome"]
    def f(s):
        return s.upper()

    print("cities:", cities)
    print(list(map(f, cities)))

    def f(s):
        return s.lower()
    print("cities:", cities)
    print(list(map(f, cities)))

    # Will call lowercase function !!
    cities = ["London", "Beijing", "Kiev"]
    print("cities:", cities)
    print(list(map(f, cities)))

    return

f1()

print("cities:", cities)
print(list(map(f, cities)))
