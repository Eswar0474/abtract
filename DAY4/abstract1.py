from abc import ABC, abstractmethod
class Demo(ABC):
    @abstractmethod
    def method(self,em):
        pass
class Test(Demo):
    def method(self,em):
        print("method",em)
t=Test()
t.method("Email")