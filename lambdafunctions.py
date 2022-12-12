sqr=lambda s:s*s
rect=lambda l,r:l*r
tri=lambda b,h:(1/2)*b*h

shape=input("Enter the shape(square,rectangle and  triangle)")
if(shape=='square'):
     a=int(input("Enter the length of the side"))
     print(sqr(a))
elif(shape=='rectangle'):
     b=int(input("Enter the length"))
     c=int(input("Enter the breadth"))
     print(rect(b,c))
elif(shape=='triangle'):
     m=int(input("Enter the breadtg"))
     n=int(input("Enter the height"))
     print(tri(m,n))
else:
     print("Please enter a valid choice")