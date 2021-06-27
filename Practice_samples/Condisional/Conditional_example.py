"""
1. Write a program that asks the user to enter a number and displays whether 
entered number is an odd number or even number?
"""

fromUser = int(input("Please enter a number"))
if(fromUser % 2 == 0):
    print("The entered number is a even number")
else:
    print("The entered number is an odd number")

# using shorthand 

print("The entered number is a even number") if fromUser % 2 == 0 else print("The entered number is an odd number")

"""

Write a program that prompts the user to input a number.
The program should then output the number and a message saying whether
the number is positive, negative, or zero.

"""

fromUser = int(input("Please enter a number"))
if(fromUser == 0):
    print("Number is equal to zero")
elif(fromUser > 0):
    print("Number is grater than zero")
else:
    print("Number is lesser than zero")

"""
Write a program to calculate the monthly telephone bills as per the following rule: 
Minimum Rs. 200 for up to 100 calls. 
Plus Rs. 0.60 per call for next 50 calls. 
Plus Rs. 0.50 per call for next 50 calls. 
Plus Rs. 0.40 per call for any call beyond 200 calls.
"""
bill = 0
telephoneUseage = int(input("Please enter the number of call"))
if(telephoneUseage <= 100 ):
    bill = 200
elif(telephoneUseage <= 150):
    bill = 200 + (telephoneUseage - 100) * 0.60
elif(telephoneUseage <= 200):
    bill = 200 + (50 * 0.60) + ((telephoneUseage - 150) * 0.60)
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (telephoneUseage - 200) * 0.40
print("Telephone bill is ",bill)