line=int(input("Enter numberbof Lines: "))
n=int(line//2)
s=(2*n)-2
for i in range(0,n):
    print("*",end="")
    for j in range(1,i):
        print(" ",end="")
    if i>0:
        print("*",end="")
    for k in range(s,(2*i),-1):
        print(" ",end="")
    if i>0:
        print("*",end="")
    for l in range(1,i):
        print(" ",end="")
    print("*")
for i in range(n,0,-1):
    print("*",end="")
    for j in range(1,i-1):
        print(" ",end="")
    if i>1:
        print("*",end="")
    for k in range((n-i)*2,0,-1):
        print(" ",end="")
    if i>1:
        print("*",end="")
    for l in range(1,i-1):
        print(" ",end="")
    print("*")

