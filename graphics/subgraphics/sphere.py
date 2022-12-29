from math import *
class sph():

    def __init__(self,r):
        self.r=r
    def spharea(self):
        return 4*pi*self.r*self.r
    def sphper(self):
        return (4/3)*pi*self.r*self.r*self.r
    
        