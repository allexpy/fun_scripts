"""
We will create a program which will calculate the area of
a chosen shape (triangle or circle).
"""
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Program is starting now!"

#Printing the time when program starts.

print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1) #delay the program

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle or S for Square: ")
option = option.upper()

#Calculating the area for a circle.
if option == 'C':
    radius = float(raw_input("Enter radius: "))
    area = pi * radius ** 2
    print "The pie is baking..."
    sleep(2)
    print ("Area: %.2f. \n%s" % (area, hint))

#Calculating the area for triangle.
elif option == "T":
    base = float(raw_input("Enter the base: "))
    height = float(raw_input("Enter the height: "))
    area = (0.5)*base*height
    print "Uni Bi Tri..."
    sleep(2)
    print ("Area: %.2f.") % (area)
    print hint
  
elif option == "S":
    side = float(raw_input("Enter the side: "))
    area = side ** 2
    print "Working..."
    sleep(2)
    print ("Area: %.2f.") % (area)
    print hint
  

else:
    print "You didn't type one of the options."

