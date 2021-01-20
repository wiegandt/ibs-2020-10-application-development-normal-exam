from fish import Fish


class Tang(Fish):

    def __init__(self, name, weight, color):
        super().__init__(name, weight, color, short_term_memory_loss=True)
        self.name = name
        self.weight = weight
        self.color = color

    def feed(self):
        super().feed()
        self.short_term_memory_loss = True
