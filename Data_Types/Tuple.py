#----------------------------------------------------
# 1. Creating an tuple  
#-----------------------------------------------------
# Creating an empty tuple  
Tuple1 = ()
print (Tuple1)  
     
# Creating a tuple of strings 
print(('Geeks', 'For'))  
     
# Creating a Tuple of list  
print(tuple([1, 2, 4, 5, 6]))
 
# Creating a nested Tuple
Tuple1 = (0, 1, 2, 3)  
Tuple2 = ('python', 'geek')  
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

#----------------------------------------------------
# 2. Accessimg elements from tuple 
#-----------------------------------------------------

tuple1 = tuple([1, 2, 3, 4, 5]) 

# Accessing element using indexing
print(tuple1[0]) 
   
# Accessing element using Negative Indexing
print(tuple1[-1])

#----------------------------------------------------
# 3. updation / deletion  elements from tuple 
#-----------------------------------------------------

tuple1 = tuple([1, 2, 3, 4, 5])
   
# Updating an element
tuple1[0] = -1
   
# Deleting an element
del tuple1[2] 
