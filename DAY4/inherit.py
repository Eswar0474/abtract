class Employee:
    def work(self):
        print("printing from employee")
class Manger(Employee):
    def manager(self):
        print("printing from manager")
m=Manger()
m.work()
m.manager()
