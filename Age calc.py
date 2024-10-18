bd=int(input("Enter Date of Birth: "))
bm=int(input("Month in 1-12: "))
by=int(input("Year: "))
cd=int(input("Enter Current Date: "))
cm=int(input("Month in 1-12: "))
cy=int(input("Year: "))
if(cm>bm):
    ay=cy-by
    if(cd>bd):
        am=cm-bm
        ad=cd-bd
    else:
        am=cm-bm-1
        ad=31-(cd-bd)
else:
    ay=cy-by-1
    if(cd>bd):
        am=12-(cm-bm)
        ad=cd-bd
    else:
        am=cm-bm-1
        ad=31-(cd-bd)
print(ay,"years",am,"months",ad,"days")
