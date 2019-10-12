#A single function that will take argument and print corresponding day of the week
#(arg = 1 to 7). Use if elif else for it

#Insert the number of the day
x = int(input("Select a number from 0 to 6 to see the corresponding day of the week: "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#The function takes a number and checks what day of the week corresponds to it:
def weekdays(x):
    if x == 0:
        print(days[0])
    elif x == 1:
        print(days[1])
    elif x == 2:
        print(days[2])
    elif x == 3:
        print(days[3])
    elif x == 4:
        print(days[4])
    elif x == 5:
        print(days[5])
    elif x == 6:
        print(days[6])

weekdays(x)

