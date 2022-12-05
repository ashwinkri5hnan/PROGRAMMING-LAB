numlist=[]
sqrlist=[]
r=int(input("enter the number of values to calculate the square of"))
print("enter ",r, "numbers")
for i in range(0,r):
    nn = int(input(""))
    numlist.append(nn)
for i in numlist:
    sqrlist.append(i**2)
print(sqrlist)