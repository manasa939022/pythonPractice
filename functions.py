def findArmstrong(number):
    sum = 0
    temp = number
    result="Number is not Armstrong"
    while temp>0:
        digit=temp%10
        sum+= digit **3
        temp//=10

    if(sum==number):
        result = "Given number is Armstrong"

    return result
def myfunc(n,a):
  return  a ** n

mytripler = myfunc(3,3)
print(mytripler)

fruits = ["apple","grapes", "banana"]
fruits.sort()
print(fruits)

result = findArmstrong(1583)
print(result)
