length=int(input("How many numbers do you want to store"))
inp=[]
print("enter the values")
for num in range(0,length):
    inp1=int(input(""))
    if inp1>100:
        inp.append("over")
    else:
        inp.append(inp1)
print(inp)