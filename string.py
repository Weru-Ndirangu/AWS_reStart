myString="This is a String."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type" +  str(type(myString)))


firststring="water"
secondstring="fall"
thirdstring=firststring + secondstring
print(thirdstring)


name= input(" What is your name? ")
print(name)


color = input(" What is your favorite color? ")
animal = input(" What is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))