### Strings are sequence of Characters ###


# str = "Akshay" #Single line String
# str1= '''
# this
# is
# multi-line
# string
# ''' #This is multi-line String

# print(str1)
# print(str)


### String Slicing ###

# str = "Akshay"
# print(str[1])
# print(str[0:3])
# print(str[0:])
# print(str[:])
# print(str[::-1]) #will reverse a string

### String Concatination ###

# str1 = "Akshay"
# str2 = "Patil"

# print(str1+" "+str2)

### String Repitition ###

# str1 = "Akshay"
# print(str1*5)

### String membership operator ###

# name = "Akshay Rajaram Patil"

# print("Akshay" in name)
# print("Patil" not in name)


### Comparison of string ###

### ASCII Values A=65 and a=97 and continue............ ###

# str1 = "Apple"
# str2 = "apple"

# print(str1>str2) #False because A has Ascii value 65 and a has 97 so, 65 is not greater than 97
# print(str1<str2)
# print(str1==str2)


### How to Get a Ascii value ###

# print(ord("A")) #65
# print(ord("B")) #66
# print(ord("a")) #97
# print(ord("b")) #98


############################ String Functions ############################


# FirstName = "akshay"
# SurName = "patil"
# test = "           hoe       "
# test2 = "Hello This is Akshay"

# print(len(FirstName))
# print(FirstName.upper())
# print(SurName.lower())
# print(FirstName.capitalize()) # Capitalizes only the first letter of the string.
# print(SurName.title()) # Capitalizes the first letter of each word in the string.
# # print(test)
# print(test.strip())
# print(test.lstrip())
# print(test.rstrip())
# print(test.replace("hoe","How are you?"))
# print(test.split(" "))
# print(" ".join(test2))
# print(test2.find("Th"))
# print(test2.startswith("H"))
# print(test2.endswith("u"))


############################ Reverse a String ############################


# str = input("Enter the String : ")
# rev = str[::-1]
# print(rev)


#way2

# rev=""
# for char in str:
#     rev = char+rev
# print(rev)

############################ Palindrome ############################

# str = input("Enter the String : ")
# if str == str[::-1]:
#     print("This is Palindrome")
# else:
#     print("Not a Palindrome")


############################ Count Vowels in a String ############################

# str = input("Enter thw Strng : ")
# count = 0
# vowels = "aeiouAEIOU"
# for char in str:
#     if char in vowels:
#         count+=1
# print(count)

############################ Format operators a String ############################

# name = "Akshay"
# age = 20
# salary = 50000.7
# print("Your name is %s and your age is %d and salary is %.2f"% (name,age,salary))
# print("your Name is {} and your age is {} and your salary is {}".format(name,age,salary))
# print(f"Your Name is {name} and Your age is {age} an your salary is {salary}")

############################ reverse a String using reversed() function ############################

# name ="car"
# print(reversed(name)) #it returns object
# print("".join(reversed(name)))

############################ words reverse ############################

# str = "Python is fun"
# print(str)
# new_str = str.split(" ")
# rev_str = " ".join(reversed(new_str))
# print(rev_str)


