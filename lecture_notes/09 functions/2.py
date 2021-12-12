cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f = lambda s: len(s)


def f1():
  cities = ['Athens', 'Roma']
  f = lambda s: s.upper()
  print({'cities': cities})
  print([f(s) for s in cities])

  if True:
    f = lambda s: s.lower()
    print({'cities': cities})
    print([f(s) for s in cities])

  if True:
    cities = ['London', 'Beijing', 'Kiev']
    print({'cities': cities})
    print([f(s) for s in cities])


f1()

print({'cities': cities})
print([f(s) for s in cities])