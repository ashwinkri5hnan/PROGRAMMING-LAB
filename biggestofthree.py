num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1>=num2 and num1>=num3:
    big=num1
elif num2>=num1 and num2>=num3:
    big=num2
else:
    big=num3
print("The biggest of three is ",big)