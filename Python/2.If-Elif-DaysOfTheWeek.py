#A single function that will take argument and print corresponding day of the week
#(arg = 1 to 7). Use if elif else for it

#Insert the number of the day
x = int(input("Select a number from 0 to 6 to see the corresponding day of the week: "))

#Take a number and check what day of the week corresponds to it:
if x == 0:
    print("Monday") 
elif x == 1:
    print("Tuesday")
elif x == 2:
    print("Wednesday")
elif x == 3:
    print("Thursday")
elif x == 4:
    print("Friday")
elif x == 5:
    print("Saturday")
elif x == 6:
    print("Sunday")
