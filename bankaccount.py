class account():
     def __init__(self,num,name,type,bal):
          self.accnumber=num
          self.name=name
          self.type=type
          self.balance=bal
     def withdraw(self,c):
          self.withdraw=c
          self.balance=self.balance-self.withdraw
     def deposit(self,d):
          self.depo=d
          self.balance=self.balance+self.depo
     def display(self):
          print("The account number is:",self.accnumber)
          print("The account holder name is: ",self.name)
          print("The account  type is: ",self.type)
          print("The balance is: ",self.balance)

x=account(128,"ashwin","savings",1200)
x.display()

ch=int(input("Enter 1 for withdrawing and 2 for depositing"))
if(ch==1):
     c=int(input("Enter the amount"))
     x.withdraw(c)
     print("Withrawed ",c,"rs")
elif(ch==2):
     c=int(input("Enter the amount"))
     x.deposit(c)
else:
     print("Please enter a valid choice")
x.display()
