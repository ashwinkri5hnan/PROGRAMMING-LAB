class publisher():
    name=''
    def __init__(self,n):
        self.name=n
    def display(self):
        print("The Publisher is ",self.name)

class book(publisher):
    title=''
    author=''
    def __init__(self,t,a,n):
        self.title=t
        self.author=a
        super().__init__(n)
    def display(self):
        super().display()
        print("The title is ",self.title)
        print("The author is ",self.author)

class python(book):
    price=0
    num=0
    def __init__(self,t,a,n,p,no):
        self.price=p
        self.num=no
        super().__init__(t,a,n)
    def display(self):
        super().display()
        print("The price is ",self.price)
        print("The number of pages are ",self.num)

h=python("haha","ashwin","DC",250,432)
h.display()