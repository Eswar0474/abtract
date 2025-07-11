class Employee:
    def set_name(self,name):
        self.__name=name
    def set_salary(self,salary):
        self.__salary=salary
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
        print(self.__name)
    def get_salary(self):
        return self.__salary
    def get_age(self):
        return self.__age
e=Employee()
e.set_name(input("Enter Employee Name:"))
try:
    age=int(input("Enter Age:"))
    while age<18 or age>100:
        age=int(input("Error: Age should be between 18 to 100 \nEnter age:"))
    e.set_age(age)
    salary=int(input("Enter Salary:"))
    while salary<0 :
        salary=int(input("Error: Salary should be above 0 \nEnter salary:"))
    e.set_salary(salary)
except ValueError:
    print("Error: Please enter a valid number")
print("Employee name : ",e.get_name())
print("Employee age: ",e.get_age())
print("Employee salary: ",e.get_salary())
