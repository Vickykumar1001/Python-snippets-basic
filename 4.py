L=[]
#Taking Input
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    x=int(input("Enter the numbers: "))
    L.append(x)

s=int(input("Enter the value to be searched: "))
c=0
for i in L:
    if(i==s):
        print("found")
        c=1
        break
if(c==0):
    print("Not found")
