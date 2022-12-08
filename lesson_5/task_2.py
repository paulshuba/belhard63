# Create calculator: user enters number_1, then operator, then number_2.
number_1 = int(input('Enter your first number: '))
oper = input('Enter operator (+, -, * or /): ')
number_2 = int(input('Enter your second number: '))
if oper == '+':
    print(number_1 + number_2)
elif oper == '*':
    print(number_1 * number_2)
elif oper == '-':
    print(number_1 - number_2)
elif oper == '/':
    print(number_1 / number_2)
else:
    print('Enter correct operator')