

class Critter(object):
    """Makes a virtual pet"""

    total = 0

    @staticmethod
    def status():
        print("\nTotal critters =", Critter.total)

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.mood = "happy"
        Critter.total += 1

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
        self.__update_mood()

    def __update_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            self.mood = "happy"
        elif 5 <= unhappiness <= 10:
            self.mood = "okay"
        elif 11 <= unhappiness <= 15:
            self.mood = "frustrated"
        else:
            self.mood = "mad"

    def eat(self, food=4):
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self) -> str:
        rep = "Critter object"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("Hi, I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()


crit = Critter("Michael")
crit.talk()
crit.talk()
for i in range(5):
    crit.talk()

crit.eat()
crit.eat()
crit.talk()

Critter.status()