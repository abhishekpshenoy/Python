""" 
File can be read using the function open in python and we should pass two parameters 
1. The path to the file eg: C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/student1.txt
2. The Mode of opening the file eg: r to specify read mode.
"""

fileReader = open("C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/test.txt","r")# read mode

# to read fist line of a file
print(fileReader.readline(),end="")
'''
here the function fileReader.readline() will read the first line of the file 
'''
# to read a complete file`  
for i in fileReader:
    print(i, end="")

fileReader.close()
# We must always use the close function after we are done with the operation of files