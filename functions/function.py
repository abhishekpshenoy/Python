"""
def function_name(parameters):
    statement(s)
"""
# def print5():
#     count = 5
#     while (count):   
#         count = count - 1
#         print("Hello World")
# print5()
# print("hi nihar")
# print5()
# print("hi Abhi")
# print5()


# def printme():
#     print("hi python")

# printme()
# printme()
# printme()
# printme()
# printme()

# docstring
# def avgof5(num1,num2,num3,num4,num5):
#     """Average of Five numbers
    
#     Avgof5 is a function that accepts five numbers 
#     and calculate the average of all this 5 numbers and prints the result"""
#     sum = num1+num2+num3+num4+num5
#     avg = sum/5
    
#     return avg

# answer = avgof5(12,23,4,56,36)
# print("average of these 5 numbers 3 ",answer)
# sum = a + b
# # x = lambda a,b : a+b
# def x(int1,int2):
#     sum = int1 + int2
#     print(sum)
# # print(x(10,20))

# x(10,20)


def addme(num1,num2):
    """A function to add two numbers"""
    sum = num1+num2
    # print("the sum of the numbers is ",sum)
    addme(sum,num1)
    return sum

# first = 100
# second = 200

# # sumoftwo = first + second 
# sumoftwo = addme(first,second)
# print(sumoftwo)
# a = 5*4*3*2*1


# ncr = n!/(n-r)!r!

# npr
def factorial(number):
    solution = 1
    while (number >= 1):
        solution = solution * (number)
        number = number - 1
    return solution

def factorial(number):
    if (number == 1):
        return 1
    else:   
        return number * factorial(number - 1)

solution = factorial(6)
print(solution)
    

# Python code to implement Fibonacci series

# Function for fibonacci
def fib(n):

    # Stop condition
    if (n == 0):
        return 0

    # Stop condition
    if (n == 1 or n == 2):
        return 1

    # Recursion function
    else:
        return (fib(n - 1) + fib(n - 2))


# Driver Code

# Initialize variable n.
n = 5
print("Fibonacci series of 5 numbers is :",end=" ")

# for loop to print the fiboancci series.
for i in range(0,n): 
    print(fib(i),end=" ")



string = "abhishek"
 
 
def test(string):
     
    string = "Nihar"
    print("Inside Function:", string)
     
# Driver's code
test(string)
print("Outside Function:", string)



def add_more(list):
    list.append(50)
    print("Inside Function", list)
 
# Driver's code
mylist = [10,20,30,40]
 
add_more(mylist)
print("Outside Function:", mylist)