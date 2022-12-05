li=[]
n=int(input("Enter the size"))
for i in range(0,n):
    li.append(int(input("")))

for m in li:
    if m%2==0:
        li.remove(m)
print(li)