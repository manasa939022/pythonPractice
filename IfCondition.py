b=2
a=4

if a > b:
    print("a greater than b")
    c=a+b
    print("sum of a  and b is",c)

marks = 90
credit = 11
if marks >=35 and marks >= 80:
    if credit<=10:
        print("student passed in distinction")
    #else:
     #   print("student passed in credits")
elif marks >= 35:
    print("Student passed in exam without credits")
elif marks >=60:
    print("c grade")
else:
    print("student failed in exam")

 #short hand if else
x = 20
y = 25

print(x-y) if x>y else  print(x+y)

