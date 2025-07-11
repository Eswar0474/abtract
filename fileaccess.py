with open('data1.txt', 'w') as file:
    file.write("this is a sample text file")
with open('data1.txt', 'r') as file:
    print(file.read())
with open('data1.txt', 'a')as file:
    file.write(" stored in data1.txt")
with open('data1.txt', 'r') as file:
    print(file.read())
