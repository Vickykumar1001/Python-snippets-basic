L=[]
#Taking Input
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    x=int(input("Enter the numbers: "))
    L.append(x)
#Printing odd position elements
print("The elements at odd positions are : ")
for i in range(1, len(L), 2):
   print(L[i])