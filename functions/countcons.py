#input ==== "Abhishek"
#output = 5


# without recurtion
def isThisCons(cha):
    # print(cha)
    # cha = cha.Upper()
    return not (cha == "A" or cha == "E" or cha == "I" or cha == "U"or cha == "O" or cha == "a" or cha == "e" or cha == "i" or cha == "u"or cha == "o") #and ord(cha) >= 65 and ord(cha) <= 90# checking if its a vowel
# # check = isThisCons("A")


def countcons(string):
    count = 0
    # loops take a string and break it to char and then pass it to the function
    print(len(string))
    for i in range(len(string)):
        if (isThisCons(string[i])):
            count += 1
    return count
# print(check)
string = "ABhishek"

# answer = countcons(string)

# print(answer)

def reccountcons(string , n):
    if n == 1:
        return isThisCons(string[0])
    return (reccountcons(string, n-1) + isThisCons(string[n - 1]))


string = "ishek"

answer = reccountcons(string, len(string))
print(answer)

