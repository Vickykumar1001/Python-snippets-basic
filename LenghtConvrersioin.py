ft = int(input("Input distance in feet: "))
print("Enter 1 to convert to inches: ")
print("Enter 2 to convert to yards: ")
print("Enter 3 to convert to miles: ")
print("Enter 4 to convert to millimeter: ")
print("Enter 5 to convert to centimeter: ")
print("Enter 6 to convert to meter: ")
print("Enter 7 to convert to kilometer: ")
c=int(input("Enter your Choice: "))
if c==1:
    inches = ft * 12
    print("The distance in inches is %i inches." % inches)
elif c==2:
    yards = ft / 3.0
    print("The distance in yards is %.2f yards." % yards)
elif c==3:
    miles = ft / 5280.0
    print("The distance in miles is %.2f miles." % miles)
elif c==4:
    milli = ft * 304.8
    print("The distance in yards is %i millimeters." % milli)
elif c==5:
    centi = ft * 30.48
    print("The distance in miles is %i centimeters" % centi)
elif c==6:
    meter = ft * 3.048
    print("The distance in yards is %i meters" % meter)
elif c==7:
    kilo = ft / 3280.8
    print("The distance in miles is %.2f kilometers." % kilo)