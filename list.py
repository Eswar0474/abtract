l=list(map(int,input("Enter your 5 numbers:").split()))
l.reverse()
print(l)
s=0
for i in l:
    s=s+i
print(s,s/(len(l)))