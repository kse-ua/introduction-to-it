class counter:
    def __init__(self, value, x):
        self.value = value
        self.x = x
    def inc(self):
        self.value += self.x
        return self.value

c = counter(0, 10)
print(c.inc())

c = counter(0, 20)
print(c.inc())
