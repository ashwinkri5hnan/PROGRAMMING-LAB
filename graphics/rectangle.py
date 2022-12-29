class rect():  
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def rectarea(self):
        return self.length*self.breadth
    def rectper(self):
        return 2*(self.length+self.breadth)
