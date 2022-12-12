def long(a):
     max=len(a[0])
     temp=a[0]
     for i in a:
          if(len(i)>max):
               max=len(i)
               temp=i
     print("The longest word is ",temp)

li=[]
n=int(input("Enter the limit of the list"))
print("Enter the strings to the list")
for i in range(0,n):
     n=input("")
     li.append(n)
long(li)