
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("I am a teacher, my name is %s, I am %d years old" % (self.name, self.age))

    def teach(self):
        print("I am teaching")


class computer_teacher(teacher):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def say(self):
        print("I am a computer teacher, my name is %s, I am %d years old, my height is %d" % (self.name, self.age, self.height))

    def coding(self):
        print("I am coding")


sir1=teacher("sir1", 30)
sir1.say()
sir1.teach()

sir2=computer_teacher("sir2", 40, 180)
sir2.say()
sir2.teach()
