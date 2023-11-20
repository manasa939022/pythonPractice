class Animal :
    name = ""
    def eat(selfself):
        print("I can eat")
# inherit from Animals
class Dog(Animal):

     # override eat() method
    def eat(self):
#call the eat() method of superclass using super()
      super().eat()
print("I like to eat bones")
# create an object of the subclass
labrador = Dog()
labrador.eat()