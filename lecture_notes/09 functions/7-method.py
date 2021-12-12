class Counter():
    value = 0

    def inc(self, x):
        self.value += x


counter = Counter()

counter.inc(10)
print({'counter': counter.__dict__})

counter.inc(20)
print({'counter': counter.__dict__})
