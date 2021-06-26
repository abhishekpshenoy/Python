A_list=["abhi","nihar","Sahana","Laya"]# list
A_list=["abhi","nihar","Sahana","Laya"]# list with range and len methord
A_tuple = (1,5,"abc","nihar")#tuple
A_int = 10# integer with range methord
A_string = "ABHISHEK" # string it converted to char
A_dict = {"name":"Abhi","company":"sigsenz","language":"python"}

# simple for statement we can use any variable declared above in for loop variable

for i in range(len(A_list)):
    print(A_list[i])

for i in A_list:
    print(i)

for i in A_tuple:
    print(i)

for i in A_string:
    print(i)# this will print each and every character

for i in A_dict:
    print(i)  # this will Print the key
    print(A_dict[i])# this will Print the value

for i in range(0,A_int): # range has a perameter called offset 
    print(i)