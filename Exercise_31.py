"""
3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.00 per hour to test the program (the pay should be 475). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
"""
hrs = raw_input("Enter Hours:")
h = float(hrs)
if h <= 40:
  total = 10 * h
else:
  total = 400 + (h-40) * 15
print "Pay:", int(total)