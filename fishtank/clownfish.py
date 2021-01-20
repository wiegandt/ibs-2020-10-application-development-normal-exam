from fish import Fish

class Clownfish(Fish):
    color2 = ""

    def __init__(self, name, weight, color, color2):
        super().__init__(name, weight, color, short_term_memory_loss=False)
        self.name = name
        self.weight = weight
        self.color = color
        self.color2 = color2
        self.short_term_memory_loss = False

    def feed(self):
        super().feed()
        return self.color2

