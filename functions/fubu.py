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

# ap , gp 
# Driver Code

# Initialize variable n.
n = 16
print("Fibonacci series of 5 numbers is :",end=" ")

# for loop to print the fiboancci series.
for i in range(0,n): 
    print(fib(i),end=" ")