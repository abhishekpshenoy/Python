#----------------------------------------------------------
# 1. Creation of List   
#----------------------------------------------------------
# Creating a List  
List = []  
print(List)  
     
# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks'] 
print(List)  
     
# Creating a Multi-Dimensional List  
List = [['Geeks', 'For'], ['Geeks']]  
print(List)

#----------------------------------------------------------
# 2. Adding Elements to a List    
#----------------------------------------------------------

# Creating a List  
List = []
     
# Using append()
List.append(1)  
List.append(2)
print(List)  
   
# Using insert()
List.insert(3, 12)  
List.insert(0, 'Geeks')
print(List)  
   
# Using extend()  
List.extend([8, 'Geeks', 'Always'])  
print(List)

#----------------------------------------------------------
# 3. Accessing elements from the List 
#----------------------------------------------------------

# accessing of element from list  
List = [1, 2, 3, 4, 5, 6]  
     
# accessing a element
print(List[0])   
print(List[2])  
   
# Negative indexing
# print the last element of list  
print(List[-1])
# print the third last element of list   
print(List[-3])

#----------------------------------------------------------
# 4. Removing Elements from the List
#----------------------------------------------------------
# Removal of elements in a List  
     
# Creating a List  
List = [1, 2, 3, 4, 5, 6,   
        7, 8, 9, 10, 11, 12]
 
# using Remove() method  
List.remove(5)  
List.remove(6)
print(List)  
   
# using pop()
List.pop()
print(List)
