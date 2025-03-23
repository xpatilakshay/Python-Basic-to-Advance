
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
