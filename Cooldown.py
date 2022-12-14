class Cooldown:

    def __init__(self, time, counter=None):
        self.time = time
        self.counter = time if counter is None else counter

    def __copy__(self):
        return Cooldown(self.time, self.counter)

    def is_ready(self):
        return self.counter == self.time

    def use(self):
        self.counter = 0

    def update(self):
        if not self.is_ready():
            self.counter += 1
