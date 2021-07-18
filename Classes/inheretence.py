# A parent class

# Encapsulation

# access specifiers they tell u if the variables can be accessed from outside the class or not 

class Person(object):
    def __init__(self,name):
        self.__name = name# private # pubilc
        print("hi i am ", name)
    def change_name(self, name, password="not"):
        if(password == "Abhishek"):
            self.__name = name
        else:
            print("Incorrect password")
    def intro(self):
        print("HI i am ",self.__name," How are u ")

class student(Person):
    def __init__(self):
        print("I was a student back then")
    def education(self):
        print("I did my BE from BMSIT")

class employee(student):
    # pass
    def __init__(self,name,companyname,id_number,jobrole):
        Person.__init__(self, name)
        student.__init__(self)
        self.__companyname = companyname
        self.__id_number = id_number
        self.__jobrole = jobrole
        # print("I am ",Person1.__name," and i am working in ",self.__companyname," as a ",self.__jobrole)

# a Child