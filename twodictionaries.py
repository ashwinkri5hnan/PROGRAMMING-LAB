dictionary1={}
n=int(input("Enter the size"))
for i in range(0,n):
    color=input("Enter the color")
    number=int(input("Enter the number"))
    dictionary1[color]=number
dictionary2={}
n=int(input("Enter the size"))
for i in range(0,n):
    color=input("Enter the color")
    number=int(input("Enter the number"))
    dictionary2[color]=number

print(dictionary1 | dictionary2)
