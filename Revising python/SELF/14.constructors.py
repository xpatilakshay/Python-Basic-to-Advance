###############  Create a student class and take name and marks of 5 subjects as argument in constructor then create  YHEN CREATE A FUNCTION TO PRINT THE AVERAGE OF MARKS ###############


############### Way 1 ###############

# class Student:
#     def __init__(self,**kwargs):
#         self.kwargs = kwargs

#     def avg(self):
#         return sum(self.kwargs.values())/len(self.kwargs)
        
# st = Student(Marathi=45,hindi=33,English=55,Geography=55,Maths=65)
# print(st.avg())

############################## way 2 ##############################

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def calculate_avg(self):
#         avg = sum(self.marks)/len(self.marks)
#         return avg

# marks = [90,80,70,60,50]
# s1 = Student("Akshay",marks)
# print(f"Student Name : {s1.name} and Average : {s1.calculate_avg()}")


# marks = [90,80,70,60,50]
# s2 = Student("Sahil",marks)
# print(f"Student Name : {s2.name} and Average : {s2.calculate_avg()}")


# marks = [90,80,70,60,50]
# s3 = Student("Rohan",marks)
# print(f"Student Name : {s3.name} and Average : {s3.calculate_avg()}")


# marks = [90,80,70,60,50]
# s4 = Student("Vishwajit",marks)
# print(f"Student Name : {s4.name} and Average : {s4.calculate_avg()}")


# marks = [90,80,70,60,50]
# s5 = Student("Suraj",marks)
# print(f"Student Name : {s5.name} and Average : {s5.calculate_avg()}")


############################## Bank Account details can be Accessed easily which is risky ##############################

# class Bank:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# b = Bank(12345,123)
# print(f"Account No : {b.acc_no} and Account Password : {b.acc_pass}")


############################## To overcome above issue we have private attribute ##############################

# class Bank:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #__(double underscore) i used to make attrubute private

# b = Bank(12345,123)
# print(f"Account No : {b.acc_no} and Account Password : {b.acc_pass}") #AttributeError: 'Bank' object has no attribute 'acc_pass' Because we have made attibute private so it is a safe practice

############################## How to access the private attributw ##############################

# class Bank:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def password(self):
#         return self.__acc_pass

# b = Bank(12345,123)
# print(f"Account No : {b.acc_no} and Account Password : {b.password()}")


############################## Creating an ATM ##############################

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance

#     def show_balance(self):
#         print(f"Your Current balance is {self.__balance}")

#     def credit(self):
#         amount = int(input("Enter the ammount to be credited : "))
#         self.__balance = self.__balance + amount
#         print(f"Your Balance After Crediting {amount}RS Amount is {self.__balance}RS")

#     def debit(self):
#         amount = int(input("Enter the amount to be debited : "))
#         if self.__balance<amount:
#             print("Insufficient Balance")
#         else:
#             self.__balance = self.__balance - amount
#             print(f"You Banlance Afer Debiting {amount}RS is {self.__balance}RS")


# ba1 = BankAccount(10000)
# ba1.show_balance()
# ba1.credit()
# ba1.debit()







