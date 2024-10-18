L=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    x=int(input("Enter the numbers: "))
    L.append(x)
Lnew=[]
for x in L:
    if x not in Lnew:
        Lnew.append(x)

for y in Lnew:
    count=0
    for z in L:
        if y==z:
            count+=1
    if count==2:
        print(y)