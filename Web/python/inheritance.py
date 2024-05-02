class Animal:
    def animal(self):
        print("are living things")
    def cat(self):
        print("drinks milk")
    def lion(self):
        print("eats meat")

class Human(Animal):
    def person(self):
        print("breath")



being = Human()

print(being.animal())
