
flights = [
  {"from: 'Kiev'" : " to 'Rome'" },
  { "from: 'Kiev'": " to 'Warsaw'" },
  { "from: 'Dublin'":" to 'Riga'" },
  { "from: 'Riga'":" to Dublin'" },
  { "from: 'Kiev'":" to 'Rome'" },
  { "from: 'Cairo'": " to 'Paris'" },
]
directions = []
for dict in flights:
    print(dict)
    if dict not in directions:
        directions.append(dict)
        
print("_")
for dict in directions:
    print(dict)


