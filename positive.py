inp=int(input("enter the size of list"))
list=[]
print("enter the values")
for i in range(0,inp):
    value=int(input(""))
    list.append(value)
print("the positive numbers in ",list,"are")
for i in list:
    if i>=0:
        print(i)