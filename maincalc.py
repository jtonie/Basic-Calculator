
num1 = float(input("Enter first number"))
op = input("Enter Operator")
num2 = float(input("Enter third number"))

if op == "+":
    print(num1 + num2)
elif op == "-":     
    print(num1 - num2)
elif op == "/":
    print( num1 / num2)
elif op == "*":
    print( num1 * num2)
else:
    print("That is not an Operator. (+ / * -)")
