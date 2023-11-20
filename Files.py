
try:
    #opening a file - defaukt mode is read 'r'
    file1=open("tesst.txt")

    #reading the contents of the file
    readcontent=file1.read()
    print(readcontent)
    file2=open("test2.txt","w")
    file2.write("This is a new file")
    file2.write("I need to learn this programming")
    file2.close()
    file2 = open("test2.txt", "r")
    content=file2.read()
    print(content)
finally:
    #closing the file to free up the resources after finishing the use of the file
    file1.close()