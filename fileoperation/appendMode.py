""" 
File can be read using the function open in python and we should pass two parameters 
1. The path to the file eg: C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/student1.txt
2. The Mode of opening the file eg: a to specify append mode.
"""

fileReader = open("C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/test.txt","a")# append mode

fileReader.write("\n -Thank You")
# Here "Thank You" is added in the last line of the file we are using "\n" which is called new line character to go to next line
fileReader.close()
# we need to close once we are don with the operation