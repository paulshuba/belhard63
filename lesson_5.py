# a = 4
# if a % 2:
#     print('this')
# else:
# #     print('that')

# numbers = [2, 3, 4, 5, 6, 2]
# while 2 in numbers:
#     numbers.remove(2)
#     print(numbers)

# text = input('input number: ')
# while not text.isdigit():
#     text = input('input number: ')
# print('congratulations, your number is: ', text)
#
# number = input()
# sum = 0
# for i in number:
#     sum += int(i)
# print("sum = ", sum)

a = int(input())
oper = input()
b = int(input())
if oper == '+':
    print(a+b)
elif oper == '*':
    print(a*b)
elif oper == '-':
    print(a - b)
elif oper == '/':
    print(a / b)
else:
    print('enter valid info')
