class Counter:
    def __init__(self):
        self.value = 0
    def inc(self, x):
        self.value += x

counter = Counter()
counter.inc(10)
print(counter.value)
counter.inc(20)
print(counter.value)