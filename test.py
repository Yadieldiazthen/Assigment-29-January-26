num1 = float(input("first number"))
num2 = float(input("second number"))
x = input("addition, subtract, multiplication, division")

if x == '+':
    answer = num1 + num2
elif x == '-':
    answer = num1 - num2
elif x == '*':
    answer = num1 * num2
elif x == '/':
    answer = num1 / num2


print(f"{answer}")