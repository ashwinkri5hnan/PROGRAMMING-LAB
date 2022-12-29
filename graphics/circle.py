from math import *
class cir():
    def __init__(self,r):
        self.r=r
    def circarea(self):
        return pi*self.r*self.r
    def circper(self):
        return 2*pi*self.r