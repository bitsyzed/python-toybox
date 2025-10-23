equation = []

print("Enter the first number.")
equation.append(input())
print("Enter the second number.")
equation.append(input())
print("Enter the operation (+, -, *, /).")
match input():
    case "+":
        equation.append("+")
    case "-":
        equation.append("-")
    case "*":
        equation.append("*")
    case "/":
        equation.append("/")



match equation[2]:
    case "+":
        print(float(equation[0]) + float(equation[1]))
    case "-":
        print(float(equation[0]) - float(equation[1]))
    case "*":
        print(float(equation[0]) * float(equation[1]))
    case "/":
        print(float(equation[0]) / float(equation[1]))