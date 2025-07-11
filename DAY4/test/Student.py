class Student:
    #setter method for name
    def set_name(self,name):
        self.__name=name
    #setter method for marks
    def set_mark(self,mark):
        self.__mark=mark
    #getter method for name
    def get_name(self):
        return self.__name
    #getter method for marks
    def get_mark(self):
        return self.__mark
#get Student details
s=Student()
s.set_name(input("Enter Student Name:"))
#try except to get only number
try:
    n=int(input("Enter marks:"))
    # contraint for marks that it should be between 0 to 100
    while n<0 or n>100:
        n=int(input("Error: Marks Should be between 0 to 100 \nEnter marks:"))
except ValueError:
    print("Invalid Input")
s.set_mark(n)
#print details
print("Student Name:",s.get_name())
print("Marks:",s.get_mark())