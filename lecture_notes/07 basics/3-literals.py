purchase = {
  'Electronics': [
    { 'name': 'Laptop', 'price': 1500 },
    { 'name': 'Keyboard', 'price': 100 },
    { 'name': 'HDMI cable', 'price': 10 },
  ],
  'Textile': [
    { 'name': 'Bag', 'price': 50 },
  ],
}

electronics = purchase['Electronics']
print(electronics)

textile = purchase['Textile']
print(textile)

bag = textile[0]
print(bag)

price = purchase['Electronics'][2]['price']
print(price)
