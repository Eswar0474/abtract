class marks:
    def __init__(self,a):
        self.__math=a
    def update(self,a):
        self.__math=a
    def display(self):
        print(self.__math)
m=marks(10)
m.display()
m.update(20)
m.display()
print(m.__math)# __math is a private variable so we can't access