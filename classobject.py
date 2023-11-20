class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is ",self.name, self.age)

p1 = Person("John", 36)
p2 = Person("Ram", 38)

p1.myfunc()
p2.myfunc()
p2.name = "SeethaRam"
p2.myfunc()
1.#Store input numbers
num1 = input("Enter first number:")
num2 = input("Enter second number:")
#Add two numbers
sum = float(num1) + float(num2)
#Display the sum
print("The sum of {0} and {1} is {2}",sum)
number =50
#check if number is greater than 0
if number > 0:
  print("Number is positive.")
print("The if statement is easy")
#import complex math module
import cmath
a = 1
b = 5
c = 6
#calculate the discriminant
d = (b**2) - (4*a*c)
#find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1}",(sol1,sol2))
def greet():
  print("Hello world")
#call the function
greet()
print("outside function")
#function with two arguments
def add_numbers(num1, num2):
  sum = num1 +num2
  print("sum: ",sum)
#function call with two values
add_numbers(5,4)
#function that adds two numbers
def add_numbers(num1, num2):
  sum = num1 +num2
  return sum
#calling function with two values
result = add_numbers(5, 4)
print("sum:",result)
import math
# sqrt computes the square root
square_root =math.sqrt(4)
print("square root of 4 is",square_root)
# pow() comptes the power
power = pow(2, 3)
print("2 to the power 3 is",power)
