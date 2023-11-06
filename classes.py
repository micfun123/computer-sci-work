class person:
    def __init__(self, name: str, age: int, money: float):
        self.name = name
        self.age = age
        self.money = money
        print("class has been initilised")

    def description(self):
        return f"{self.name} is {self.age} years old"


michael = person("michael", 16, 2.50)


print(michael)

print(michael.description())
