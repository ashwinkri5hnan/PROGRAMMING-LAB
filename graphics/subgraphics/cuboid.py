class cuboi():
    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def cubarea(self):
        return 2*self.l*self.w+2*self.w*self.h+2*self.l*self.h
    def cubper(self):
        return 4*(self.l+self.h+self.w)
