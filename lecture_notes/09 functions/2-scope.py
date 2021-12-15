cities = ["Athens", "Roma", "London", "Beijing", "Kiev", "Riga"]

func = len

def f1():
    cities = ["Athens", "Roma"]
    func = str.upper

    print("cities: ", cities)
    print(list(map(func, cities)))

    func = str.lower
    print("cities: ", cities)
    print(list(map(func, cities)))

    func = str.upper
    cities = ["London", "Beijing", "Kiev"]
    print("cities: ", cities)
    print(list(map(func, cities)))


f1()

print(list(map(func, cities)))