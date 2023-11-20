greet = lambda name:print("My name is ",name)
greet("Supriya")

#Using filter with lambda functions
#returns the list for which the function returns true
numlist=list(range(21))
newlist = list(filter(lambda x:(x%2==0),numlist))
print(newlist)

#Using map with the lamda functions
doublelist=list(map(lambda x:x*2,numlist))
print(doublelist)