
"""
NOTE  nested-if

if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here


"""
Marks = 90
Grade_A = 90
Grade_B = 80
Grade_C = 70
PassingMarks = 40

if (Marks >= PassingMarks):
    if(Marks >= Grade_C):
        if(Marks >= Grade_B):
            if(Marks >= Grade_A):
                print(" The student has scored A ")
            else:
                print(" The student has scored B ")
        else:
            print("Student has scored a C")
    else:
        print(" The student has Cleared the exam ")
else:
    print("student has failed in the exam")
