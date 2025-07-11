def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("error : divided by zero")
        return
a=10
b=0
print(divide(a,b))