
################## Control Flow Statements ##################


################## For loop ##################

# n = int(input("Enter the number :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print("Even",i)


################## While loop ##################


# n = int(input("Enter the number : "))
# i=2
# while i<n+1:
#     if i%2==0:
#         print("Even",i)
#     i=i+1


################## max Number ##################

# nums = [1,2,3,4,5,6,7,8,9]
# max = 0
# for num in nums:
#     if num>max:
#         max = num
# print(max)

################## Total of numbers ##################

# nums = (1,2,3,4,5,6,7,8)
# total = 0
# for i in nums:
#     total = total + i
# print(total)

################## Count no of characters in String without space ##################

# str = "Akshay patil"
# count = 0 
# for char in str:
#     if char != " ":
#         count+=1
# print(count)

################## Traversing Dictionary ##################

# student = {"name":"Akshay","age":20}
# for key,value in student.items():
#     print(key,value)


################## Even numbers between 2 numbers ##################

# n1 = int(input("Enter the first Number : "))
# n2 = int(input("Enter the second Number : "))

# print("even Numbers are : ")
# for i in range(n1,n2):
#     if i%2==0:
#         print(i)


################## Break Keyword with while loop ##################

# while True:
#     n = input("Enter the number : ")
#     if n:
#         print(n)
#     else:
#         break

################## Break Keyword with while loop with bool ##################

# is_active = True
# while is_active:
#     n = input("Enter the Name : ")
#     if n:
#         print(n)
#     else:
#         is_active = False

################## Break ##################

# for i in range(0,10):
#     print(i,end=" ")
#     if i == 5:
#         break
#     # print(i,end=" ")

################## Break ##################

while True:
    n = int(input("Enter the number greater than 0 : "))
    if n>0:
        break
print(n)
