""""
'use strict';

const cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga'];
const f = (s) => s.length;

function f1() {
  const cities = ['Athens', 'Roma'];
  const f = (s) => s.toUpperCase();

  console.dir({ cities });
  console.dir(cities.map(f));

  {
    const f = (s) => s.toLowerCase();
    console.dir({ cities });
    console.dir(cities.map(f));
  }

  {
    const cities = ['London', 'Beijing', 'Kiev'];
    console.dir({ cities });
    console.dir(cities.map(f));
  }
}

f1();

console.dir({ cities });
console.dir(cities.map(f));
"""

# ----------------------------------------------------------------------

cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda x: str.__len__(x)

def f1():
    cities = ['Athens', 'Roma']
    f = lambda x: str.upper(x)

    print('cities:', cities)
    print(list(map(f, cities)))

    def f1_():  
        f = lambda x: str.lower(x)
        print('cities:', cities)
        print(list(map(f, cities)))
        return

    f1_()  # nested function execution

    cities = ['London', 'Beijing', 'Kiev']
    print('cities:', cities)
    print(list(map(f, cities)))  # f - the top external function will be executed



f1()
print('cities:', cities)  # external list of cities
print(list(map(f, cities)))  # f - the top external function will be executed
