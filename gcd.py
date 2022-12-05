def hcf(a, b):
    if (b == 0):
        return a
    else:
        return hcf(b, a % b)
a = int(input("Enter a number"))
b = int(input("enter the second number"))
print("The gcd of ",a,"and",b," is : ", hcf(a,b))
