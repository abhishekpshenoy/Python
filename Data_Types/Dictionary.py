# Creating an empty Dictionary  

Dict = {}
# with Integer Keys  
Dict = {1: 'Student1', 2: 'Student2', 3: 'Student3'}
print(Dict)  
# with Mixed keys  
Dict = {'Name': 'Abhi', 1: [1, 2, 3, 4]}
print(Dict) 

#---------------------------------------------------------------------------------------------- 
# 1. There are two ways of accessing an element from a Dictionary   
#----------------------------------------------------------------------------------------------

# Creating a Dictionary   
Dict = {1: 'Student', 'name': 'Abhi', 3: 'ECE'}  
# accessing a element using key
print(Dict['name'])  
# accessing a element using get()
print(Dict.get(3)) 

#----------------------------------------------------------------------------------------------
# 2. Adding elements one at a time 
#----------------------------------------------------------------------------------------------

Dict[0] = 'Abhi'
Dict[2] = 'CS'
Dict[3] = 1
print(Dict) 
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print(Dict) 

#----------------------------------------------------------------------------------------------
# 3. accessing an element from a Dictionary   
#----------------------------------------------------------------------------------------------

# Creating a Dictionary   
Dict = {1: 'Student', 'name': 'Abhishek', 3: 'ECE'}  
# accessing a element using key
print(Dict['name'])  
# accessing a element using get()
print(Dict.get(3)) 

#----------------------------------------------------------------------------------------------
# 4. Removing elements from Dictionary
#----------------------------------------------------------------------------------------------

# Initial Dictionary  
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',  
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
       }  
# using pop()  
Dict.pop(5) 
print(Dict)  
# using popitem()  
Dict.popitem() 
print(Dict)  

#----------------------------------------------------------------------------------------------
# 5. Nested Dictionary
#----------------------------------------------------------------------------------------------

# Creating a Nested Dictionary  
# as shown in the below image 
Dict = {1: 'Abhi', 2: 'For',3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'India'}} 
print(Dict)  



#----------------------------------------------------------------------------------------------



