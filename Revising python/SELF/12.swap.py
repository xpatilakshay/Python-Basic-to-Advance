################# First Way using temporary variable #################

print("===================================================================")
a = 2
b = 6
print(f"before a and b are {a} and {b} respectively")
temp = a
a = b
b = temp

print(f"After a and b are {a} and {b} respectively")

print("===================================================================")
################# Second Way #################

a = 2
b = 6
print(f"before a and b are {a} and {b} respectively")
a,b = b,a
print(f"After a and b are {a} and {b} respectively")

print("===================================================================")