names=["Ram","Rahim","John","Sita","Varun","Deepu"]
names.append("Kiran")
print(names)
names.insert(2,"Kavitha")
print(names)
names2=["Hari","Giri","Supriya","Teja"]
#names.append(names2)
#print(names)
names.extend(names2)
print(names)
#list is mutable - changebale

names[4]="Sarita"
print(names)
#remove elements from the list

names.remove("Sarita")
print(names)
#using pop without index
print(names.pop())

#pop using index
print(names.pop(4))

#using del

del names[0:2]
print(names)

names.sort()

print(names)

desnames=sorted(names, reverse=True)

print(desnames)

desnames.reverse()

print(desnames)

print("length of the desnames is",len(desnames))