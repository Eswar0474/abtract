class Test():
    def method(self,a=None,b=None,c=None):
        if a and b and c:
            print("3")
        elif a and b:
            print("2")
        else:
            print("1")
t=Test()
t.method(1)
t.method(1,2)
t.method(1,2,3)