# 15. Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month
#     name form that variable.
from datetime import datetime
import calendar

curDateTime = datetime.now()
print(curDateTime)
month_num = curDateTime.month
print(calendar.month_name[month_num])

#16. Write a simple function that takes 2 parameters -- a  first name and a day name.
#    - Set a default value for the day name of Sunday.
#    - Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.  
#    - Invoke this function with 2 variables.
#    - Invoke this function with 1 variable only.

def printGreeting(fName,dName="Sunday"):
    print("Hi " + fName + "! Happy " + dName)

printGreeting("Jason", "Friday")
printGreeting("Bob")

# 17. Write a block of code to handle one of the most common Python exception errors. Select one of the common errors 
# from the curriculum section on Python Exception handling. Have your code example uses the `try`,`except`, `else`, and
#  `finally` components.

try:
    print(x)
except NameError:
    print("Variable was not defined")
except:
    print("There was another error")
else:
    print("There was no error")
finally:
    print("This always gets printed whether there is an error or not")