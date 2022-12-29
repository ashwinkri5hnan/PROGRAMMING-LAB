from rectangle import rect
import circle
from subgraphics.cuboid import *
from subgraphics.sphere import sph

l=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadth of the rectangle"))
haha=rect(l,b)
val=haha.rectarea()
val2=haha.rectper()
print("The area is ", val)
print("The perimeter is",val2)

r=int(input("Enter the radius of the circle"))
huhu=circle.cir(r)
val=huhu.circarea()
val2=huhu.circper()
print("The area is ", val)
print("The perimeter is",val2)

l=int(input("Enter the length of the cuboid"))
w=int(input("Enter the width of the cuboid"))
h=int(input("Enter the height of the cuboid"))

hehe=cuboi(l,w,h)
print("The area is ",hehe.cubarea())
print("The perimeter is ",hehe.cubper())

r=int(input("Enter the radius of the sphere"))
hihi=sph(r)
print("The area is ",hihi.spharea())
print("The perimeter is ",hihi.sphper())