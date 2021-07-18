# def printme( name):
#     print("My name is ", name)
# try:
#     printme("Abhishek")
#     printme("abhishek","Raghu")
# except:
#     print(" an error was detected")


def printme( name):
    print("My name is ", name)
try:
    printme("Abhishek")
    printme("abhishek","Raghu")
except Exception as error:
    print(" an error was detected",error)