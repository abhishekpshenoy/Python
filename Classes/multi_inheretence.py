# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
    def grandfather(self):
        print("my grandfather is ",self.grandfathername)

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
    def father(self):
        print("my father is ",self.fathername)
        

# Derived class
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
    def intro(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

