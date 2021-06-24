'''
Having the knowlage about variables we can have a few operations over these numarical variables
that is shown below
'''
# Arthimatic operations 

a = 20
b = 10

add = a + b    #   addition
sub = a - b    #   substraction
mul = a * b    #   mulitplication
div_f = a / b  #   division whose return is float
div_I = a // b #   division whose return is float
mod = a % b    #   modulo of both the numbers
print("The value of  variable a is ", a, " and b is ",b)
print("The output is addition(+) is ",add)
print("The output of substraction(-) is ",sub)
print("The output of mulitplication is ", mul)
print("The output of division whose return is float is ",div_f)
print("The output of division whose return is floatis ",div_I)
print("The output of modulo is ", mod)



# Relational Operaters this compares value and returns boolean values

a = 20
b = 10
   
# a > b is greater than
print(a > b) 
   
# a < b is lesser than
print(a < b) 
   
# a == b is logical equal to
print(a == b) 
   
# a != b is not equal
print(a != b) 
   
# a >= b is  greater than or equal to
print(a >= b) 
   
# a <= b is  lesser than or equal to
print(a <= b)



# Logical Operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations.


# both the inputs are boolean
a = True
b = False

# logical and 
print(a and b) 
   
#  a or b is True that is logical 
print(a or b) 
   
# not a is negation  
print(not a) 



# Bitwise operators: Bitwise operator acts on bits and performs bit by bit operation

a = 10
b = 4
   
# Print bitwise AND operation   
print(a & b) 
   
# Print bitwise OR operation 
print(a | b) 
   
# Print bitwise NOT operation  
print(~a) 
   
# print bitwise XOR operation  
print(a ^ b) 
   
# print bitwise right shift operation  
print(a >> 2) 
   
# print bitwise left shift operation  
print(a << 2)

#   Assignment operators: Assignment operators are used to assign values to the variables. that is =
a = 10 # this is an assignment operater wich assigns a to 10
#   Special Operaters
a1 = 'Abhishek'
b1 = 'Lets leaen '
 
# Identity operator
print(a1 is not b1)
print(a1 is b1)
 
# Membership operator
print("abhi" in a1)
print("N" not in b1)