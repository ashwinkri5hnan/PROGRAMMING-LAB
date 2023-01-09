class time:
     __hour=0
     __minute=0
     __second=0
     def __init__(self,h,m,s):
          self.__hour=h
          self.__minute=m
          self.__second=s


     def __add__(self,other):
          return self.__hour+other.__hour+self.__minute+other.__minute+self.__second+other.__second
t1=time(1,2,3)
t2=time(4,5,6)
z=t1+t2
print(z)
