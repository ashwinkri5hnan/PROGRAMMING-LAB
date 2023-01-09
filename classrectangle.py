class rectangle():
     def __init__(self,length,breadth):
          self.length=length
          self.breadth=breadth
     def area(self):
          return self.breadth*self.length
     def perimeter(self):
          return 2*(self.breadth+self.length)

a=int(input("Enter the length of the first rectangle:"))
b=int(input("Enter the breadth of the first retangle: "))
obj=rectangle(a,b)
print("The area and perimeter of the  first rectangle is:",obj.area(),"\n",obj.perimeter())
m=obj.area()
c=int(input("Enter the length of the second rectangle:"))
d=int(input("Enter the breadth of the second retangle: "))
obj=rectangle(c,d)
print("The area and perimeter of the  second rectangle is:",obj.area(),"\n",obj.perimeter())
n=obj.area()
if(m>n):
     print("Area of rectangle 1 is greater")
elif(m==n):
     print("Area of both the rectangles are same")
else:
     print("Area of rectangle 2 is greater")


