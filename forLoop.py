numbers = [2,8,7,6,11,12,90]
for n in numbers:
    if n%2==0:
        print(n, "is even", n*n)
        continue
    print(n,"is odd",n*n*n)
evenlist = []
oddlist = []
for x in range(6,101):

    if x%2==0:
        evenlist.append(x)
    else:
        oddlist.append(x)
else:
  print(evenlist)
  print("odd number list between 0 and 101:",oddlist)
