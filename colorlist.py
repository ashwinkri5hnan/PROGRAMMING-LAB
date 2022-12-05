colorlist1=[]
colorlist2=[]
n1=int(input("Enter the size of the first color list"))
print("Enter the colors")
for i in range (0,n1):
    insert=input("")
    colorlist1.append(insert)
n2=int(input("Enter the size of the second color list"))
print("Enter the colors")
for j in range (0,n2):
    insert1=input("")
    colorlist2.append(insert1)
a=set(colorlist1+colorlist2)
b=a-set(colorlist2)
print(b)