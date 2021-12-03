def distinct(dataset):
    directions = []
    for direction in dataset:
        if direction not in directions:
            directions.append(direction)
    print(f"directions:\n {directions}")


flights = [
  {'from': 'Kiev', 'to': 'Rome'},
  {'from': 'Kiev', 'to': 'Warsaw'},
  {'from': 'Dublin', 'to': 'Riga'},
  {'from': 'Riga', 'to': 'Dublin'},
  {'from': 'Kiev', 'to': 'Rome'},
  {'from': 'Cairo', 'to': 'Paris'},
]

distinct(flights)
