from clownfish import Clownfish
from tang import Tang
from kong import Kong
from fish import Fish


class Aquarium:

    def __init__(self):
        self.fishList = []

    def addFish(self, morefish):
        for fish in morefish:
            self.fishList.append(fish)

    def feed(self):
        return clownfish.feed(), tang.feed(), kong.feed()

    def removeFish(self):
        for fish in self.fishList:
            if fish.weight >= 11:
                self.fishList.remove(fish)

    def getStatus(self):
        for fish in self.fishList:
            print(Fish.status())


clownfish = Clownfish("Nemo", 5, "red", "white")
tang = Tang("Fred", 7, "blue")
kong = Kong("Peter", 9, "red")

