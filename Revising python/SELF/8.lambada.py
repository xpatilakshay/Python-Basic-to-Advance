
### Lambda is a small anonymous function ###
### it can have multiple arguments but only a single paramerter ###

# add = lambda a,b:a+b
# print(add(1,2))

### Default Argument ###

# mul = lambda a,b=3:a*b
# print(mul(2))

# mul = lambda a=2,b=3:a*b
# print(mul(6,4))

### Lambda Functions ###

# filter : used to filter elements based on specific condition

# colle = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda a : a%2==0,colle)) 
# print(even)

# Map : Used to apply function to all elements in collection

# colle = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(lambda x:x**2,colle))
# print(square)

#sorted : used to sort the element on a custom key

# collec = [("Akshay",99),("Sahil",100),("Rohan",100),("Om",99),("Raj",99)]
# sort = sorted(collec,key = lambda x : x[1])
# print(sort)

### Sorting in descending order ###

# collec = [("Akshay",99),("Sahil",100),("Rohan",100),("Om",99),("Raj",99)]
# sort = sorted(collec,key = lambda x : x[1],reverse=True)
# print(sort)

''' reduce() is a function from the functools module that reduces a list to '
'a single value by applying a function cumulatively to its elements.'''

# from functools import reduce

# lst = [1,2,3,4,5,6,7,8,9,10]
# addition = reduce(lambda x,y : x+y,lst,1)
# print(addition)