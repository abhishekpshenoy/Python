
"""

NOTE if-elif-else ladder

if (condition):
    statement
elif (condition):
    statement
.
.
.

else:
    statement

"""

Marks = 90
Grade_A = 90
Grade_B = 80
Grade_C = 70
PassingMarks = 40

if(Marks > Grade_A):
    print("Student has scored A")
elif(Marks > Grade_B):
    print("Student has scored B")
elif(Marks > Grade_C):
    print("Student has scored C")
elif(Marks > PassingMarks):
    print("Student has passed")
else:
    print("student has field")