a=input("Enter a word")
for i in range(1,len(a)):
    if(a[i]==a[0]):
        b=a[1:len(a)].replace(a[i],"$")
print(a[0]+b)