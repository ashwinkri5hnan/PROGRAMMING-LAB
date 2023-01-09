class rectangle():
     area=0
     __length=0
     __breadth=0

     def __init__(self,l,b):
          self.__length=l
          self.__breadth=b

     def area(self):
          self.area=self.__breadth*self.__length



     def __lt__(self, other):
          if self.area>other.area:
               print("The area of Rectangle 1 is greater")
          else:
               print("The area of Rectangle 2 is  greater")

print("Enter l and b of 1st rectangle")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
rect1=rectangle(l,b)
rect1.area()
print("The area of the first rectangle is ",rect1.area)

print("Enter l and b of 2nd rectangle")
l=int(input("Enter length"))
b=int(input("Enter breadth"))
rect2=rectangle(l,b)
rect2.area()
print("The area of the second rectangle is ",rect2.area)
rect1<rect2
