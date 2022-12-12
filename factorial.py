fact = 1
num = int(input("Enter a number to calculate the value of"))
if (num < 0):
     print("Factorial does not exist")
elif (num == 0):
     print("factorial of 0 is 1")
else:
     for i in range(1, num + 1):
          fact = fact * i
     print("The factorial of", num, " is", fact)
