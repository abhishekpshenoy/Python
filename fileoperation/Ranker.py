# Import Module
import os
# Folder Path to check for files
path = "C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/scores" 
# Dictionary to store all data of a student
studentData = {}
# Change the directory
os.chdir(path)

# Functions

def writeResult(FinalData):
    """Used to write the final Dictonry to a file named Result.txt"""
    with open("C:/Users/USER/Documents/Abhishek_workspace/Course/python/Python/fileoperation/Result.txt", 'w') as fileReader: 
        for key, value in FinalData.items(): 
            fileReader.write('%s \n' % (key))
            for key1, value1 in FinalData[key].items():
                fileReader.write('%s - %s \t ' % (key1,value1))
            fileReader.write('\n')
    fileReader.close()

def findScore(student):
    """Used to calculate the Percentage of student

    Inputs :- A Dictonary of scores of indivisual students
    Output :- returns the Percentage of that student
    This reads indivisial scores of each subject of a perticular student and calculates the Percentage of there scores
    """
    total = 0
    listOfScores = student.values()
    for score in listOfScores:
        total += float(score)
    return total/len(listOfScores)

def read_text_file(file_path,name):
    """ Converts text file to Dictionary.

    Input :- file path and name of the student
    Output :- Appends/Adds new student to studentData dictonary
    read_text_file is a function used to read a file convert the content of the file to Dictionary
    This function internally calls find Score and add's percentage to the dictionary as well

    """
    a_file = open(file_path)
    a_student ={}
    for line in a_file:
        key, value = line.split()
        a_student[key] = value
    a_file.close()
    if bool(a_student):
        a_student["Percentage"] = findScore(a_student)
        studentData[name] = a_student
    else:
        print("Student data is empty in ",name)
    
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        # call read text file function
        read_text_file(file_path,file[:-4])

print(studentData)
writeResult(studentData)

