import Foundation

let cities: [String] = ["Athens", "Roma", "London", "Beijing", "Kiev", "Riga"]
let citiesLengths: [Int] = cities.map {$0.count}

func f1() {
    let cities: [String] = ["Athens", "Roma"]
    var cityUpper: [String] = []
    for city in cities {
        cityUpper.append(city.uppercased())
    }

    print(cities)
    print(cityUpper)

    var cityLower: [String] = []
    for city in cities {
        cityLower.append(city.lowercased())
    }

    print(cities)
    print(cityLower)

    let citiesTwo: [String] = ["London", "Beijing", "Kiev"]
    var cityUpperTwo: [String] = []
    for city in citiesTwo {
        cityUpperTwo.append(city.uppercased())
    }
    print(citiesTwo)
    print(cityUpperTwo)
}

f1()

print(cities)
print(citiesLengths)
