class Calculator:
    # method for Addition
    def Addition(self,a,b):
        return a+b
    # method for Subtraction
    def Subtraction(self,a,b):
        return a-b
    #method for Multiplication
    def Multiplication(self,a,b):
        return a*b
    # method for Division
    def Division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
c=Calculator()
print("Addition (10 + 5): ",c.Addition(10,5))
print("Subtraction (10 - 5): ",c.Subtraction(10,5))
print("Multiplication (10 * 5): ",c.Multiplication(10,5))
print("Division (10 / 5): ",c.Division(10,5))
print("Division (10 / 0): ",c.Division(10,0))