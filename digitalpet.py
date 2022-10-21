from random import choices
from ssl import Options




class pet:
    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age

    def get_type(self) -> str:
        return self.type

    def age(self) -> int:
        self.age = self.age + 1
        return self.age


pet.name = input("Enter a pets name")
pet.type = input("Enter a pets type")
pet.age = 0



