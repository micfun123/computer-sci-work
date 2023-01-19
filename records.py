from collections import namedtuple

student_names = namedtuple('student_names' ,'first_name sirname age') 
st1 = student_names("michael", "parker", 100)
print(st1)
print(st1.age)