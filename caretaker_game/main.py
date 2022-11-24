

class Critter(object):
    """Makes a virtual pet"""
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.mood = "happy"

    def __str__(self) -> str:
        rep = "Critter object"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Hi, I'm", self.name, "and I feel", self.mood, "now.\n")

crit = Critter("Michael")
crit.talk()