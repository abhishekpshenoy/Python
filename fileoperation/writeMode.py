""" 
File can be read using the function open in python and we should pass two parameters 
1. The path to the file eg: C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/student1.txt
2. The Mode of opening the file eg: w to specify Write mode.
"""

fileReader = open("C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/test.txt","w")# write mode

fileReader.write("Hi All, I am Abhishek")
"""
Here "Hi All, I am Abhishek" is writen in a file speicified 
if there is no file this will create a file in that name in that specified location

If the file already exists then all content of the file will be deleted,
 only what is to be written will be saved therefore we need to be carefull
"""
fileReader.close()
# This is to close once we are done