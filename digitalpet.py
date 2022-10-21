from ssl import Options


pet = ""

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
print("enter a option")
options = ["start game","exit",'make new pet']

for i in options:
    print(i)
    
user_option = input()

while user_option not in options:
    user_option = input("enter a valid option \n")

