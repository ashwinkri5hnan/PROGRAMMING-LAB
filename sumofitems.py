li=[]
s=0
n=int(input("Enter the limit"))
print("Enter the elemens to the list")
for i in range(0,n):
     num=int(input(""))
     s=s+num
     li.append(num)
print("The list is ",li)
print("The sum of the items of the list is ",s)