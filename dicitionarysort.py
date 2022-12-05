dictionary={}
n=int(input("Enter the size"))
for i in range(0,n):
    color=input("Enter the color")
    number=int(input("Enter the number"))
    dictionary[color]=number

sorteddict=sorted(dictionary.values())
print("The ascending order is ",sorteddict)
sorteddict=sorted(dictionary.values(),reverse=True)
print("The descending order is ",sorteddict)