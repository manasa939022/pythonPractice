class Animal:
# attribute and method of the parent class name = ""
 def eat(self):
  print("I can eat")
# inherit from Animal
class Dog(Animal):
# new method in subclass
 def __init__(self,name):
    self.name = name
 def display(self):
# access name attribute of superclass using self
  print("My name is ",self.name)
# create an object of the subclass
labrador = Dog("Rohu")
# access superclass attribute and method
labrador.name = "Tom"
labrador.eat()
# call subclass method
labrador.display()