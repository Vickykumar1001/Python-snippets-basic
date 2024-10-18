L=[1,3,4,6,10,7,2,12]
print("Orignal List: ",L)
L.sort()
new_L=[]
for i in range(0,3):
    new_L.append(L[i])
for i in range(-1,-3,-1):
    new_L.append(L[i])
print("Required list: ",new_L)