li = [1, 3, 9, 10]
print(li[2])
try:
    a=int(input("Enter a "))
    b=int(input("Enter b"))
    sum = a+b
    print(sum)
except ValueError:
    print("Please enter only numerical number")
    try:
        a = int(input("Enter a "))
        b = int(input("Enter b"))
        sum = a + b
        print(sum)
    except ValueError:
        print("Please enter only numerical number")


