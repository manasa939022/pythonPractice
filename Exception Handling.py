try:
    num = int(input("Enter the num"))
    den = int(input("Enter the den"))
    ans = num/den
    print(ans)
except ZeroDivisionError:
    print("cant divide by zero")
    try:
        den = int(input("Enter the den"))
        ans = num/den
        print(ans)
    except ZeroDivisionError:
        print("cant divide by zero")
        den = int(input("Enter the den"))
