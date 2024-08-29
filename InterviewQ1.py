# Write a python program to find the common letter bewteen two strings
def common_letters():
    str1 = input("Enter first string ")
    str2 = input("Enter second string ")
    s1 = set(str1) # set removes the duplicate letters in it
    s2 = set(str2) # that why we convert it into set
    lst = s1 & s2
    print("Common string between two string is  := ",lst)
common_letters()