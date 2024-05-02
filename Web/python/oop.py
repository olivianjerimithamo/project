#object oriented programming
#self parameter
#object entry in a class
class People:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

person1 = People("Cate", 16, "student")
person2 = People("Jay", 30, "doctor")
person3 = People("Bet",22,"accountant")

print(f"Hi my name is {person1.name}")
#print(person1.name)


