

class Critter(object):
    """Makes a virtual pet"""

    total = 0

    @staticmethod
    def status():
        print("\nTotal critters =", Critter.total)
        
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.mood = "happy"
        Critter.total += 1

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        self.update_mood()


    def __str__(self) -> str:
        rep = "Critter object"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Hi, I'm", self.name, "and I feel", self.mood, "now.\n")

crit = Critter("Michael")
crit.talk()

Critter.status()