L=[1,3,4,6,1,7,3,4,12]
print("Orignal List: ",L)
new_L=[]
for c in L:
    if c not in new_L:
        new_L.append(c)
new_L.sort()
print("Unique sorted list: ",new_L)
