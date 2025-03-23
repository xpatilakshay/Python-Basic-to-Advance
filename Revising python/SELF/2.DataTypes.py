#################### 1 Interger Data Types ####################

####### INTEGERS #######

a = 10
print(a)
print(type(a))

####### FLOATS #######

b = 10.5
print(b)
print(type(b))

####### COMPLEX #######

c = 2+3j
print(c)
print(type(c))

#################### 2 Sequence Data Types ####################

########## string ##########

str = "Akshay Patil"
print(str)
print(type(str))

########## List ##########

lst = [1,2,3,4,5,6,7,8,9,10]
print(lst)
print(type(lst))

########## tuple ##########

tpl = (1,2,3,4,5,6,7,7,8,9)
print(tpl)
print(type(tpl))

#################### 3 Set Data Types ####################

########## Set ##########

set1 = {1,2,3,3,4,5,6,7,8}
print(set1)
print(type(set1))

########## Frozen Set ##########

fset = [8,7,6,5,4,3,2,1]
fset = frozenset(fset)
print(fset)
print(type(fset))

#################### 4 Map Data Type ####################

dict1 = {"name":"Akshay","Age":20}
for key,value in dict1.items():
    print(key,value)

print(dict1)
print(type(dict1))


#################### 5 Boolean Data Type ####################

a = True
print(a)
print(type(a))
