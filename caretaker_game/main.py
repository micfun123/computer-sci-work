class Critter(object):
    """Makes a virtual pet"""

    total = 0

    @staticmethod
    def status():
        print("\nTotal critters =", Critter.total)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name changed.")

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


crit = Critter(str(input("Enter a name for your critter: ")))
farmcrits = []
farmcrits.append(crit)
chosen = None
while chosen != "0":
    print(
        """
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        4 - Critter status
        5 - Change critter name
        6 - add critter
        7 - change critter
        8 - list critters
        """
    )

    chosen = input("Choice: ")

    if chosen == "0":
        print("Good-bye.")
    elif chosen == "1":
        crit.talk()
    elif chosen == "2":
        intfood = int(input("How much food do you want to give your critter?"))
        crit.eat(intfood)
    elif chosen == "3":
        crit.play()
    elif chosen == "4":
        Critter.status()
    elif chosen == "5":
        crit.name = str(input("What do you want to name your critter?"))
    elif chosen == "6":
        crit = Critter(str(input("Enter a name for your critter: ")))
        farmcrits.append(crit)
    elif chosen == "7":
        entercritsname = input("Enter the name of the critter you want to change: ")
        for i in farmcrits:
            if i.name == entercritsname:
                crit = i
                print("Critter changed.")
    elif chosen == "8":
        for i in farmcrits:
            print(i)

    else:
        print("Sorry, but", chosen, "isn't a valid choice.")


Critter.status()
