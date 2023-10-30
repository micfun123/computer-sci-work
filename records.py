from collections import namedtuple

student_names = namedtuple('student_names' ,'first_name sirname age') 
st1 = student_names("michael", "parker", 10)
print(st1)
print(st1.age)

#edit age
st1 = st1._replace(age=20)
print(st1.age)

#opp example
class student:
    def __init__(self, first_name, sirname, age):
        self.first_name = first_name
        self.sirname = sirname
        self.age = age

    def __str__(self) -> str:
        return f"{self.first_name} {self.sirname} {self.age}"

st2 = student("michael", "parker", 10)
print(st2)
print(st2.age)