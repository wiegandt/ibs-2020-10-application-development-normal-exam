class Fish:

    def __init__(self, name, weight, color, short_term_memory_loss=False):
        self.name = name
        self.weight = weight
        self.color = color
        self.short_term_memory_loss = short_term_memory_loss

    def feed(self):
        self.weight += 1

    def status(self):
        print("Name: " + self.name +
              "Weight: " + self.weight +
              "Color: " + self.color +
              "Memory loss: " + self.short_term_memory_loss)
