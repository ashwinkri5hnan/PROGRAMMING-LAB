import math

def even(num):
    while num>0:
        s=num%10
        if s%2==0:
            k=True
        else:
            k=False
            break
        num=num//10
    return k
n=str(input("Enter the range using comma")).split(',')
li=[]
if len(n[0])!=4 and len(n[1])!=4:
    print("Please enter a 4 digit value")
else:
    for i in range(int(n[0]),int(n[1])+1):
        srt=math.sqrt(i)
        if i%srt==0 and even(i):
            li.append(i)
    print(li)


