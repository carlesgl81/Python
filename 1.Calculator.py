#Add Number1
num1 = int(input("Enter First Number: "))

#Add Number2
num2 = int(input("Enter Second Number: "))

#Add task 
operation = int(input("Select your operation: for SUM Press 1, For SUB Press 2, For MUL Press 3, For DIV Press 4: "))

#Operation
if operation == 1:
    a = num1+num2
    print(a)

elif operation == 2:
    b = num1-num2
    print(b)

elif operation == 3:
    c = num1*num2
    print(c)

elif operation == 4:
    d = num1/num2
    print(d)