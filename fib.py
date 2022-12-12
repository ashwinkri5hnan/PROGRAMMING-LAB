nterms=int(input("How many terms??"))
n1=0
n2=1
count=0
if nterms<=0:
     print("Enter a positive term")
elif nterms==1:
     print(n1)
else:
     print("Fibonacci series is ")
     while count<nterms:
          print(n1)
          f=n1+n2
          n1=n2
          n2=f
          count+=1