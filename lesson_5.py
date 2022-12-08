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
# # print("sum = ", sum)
#


# a = int(input())
# oper = input()
# b = int(input())
# if oper == '+':
#     print(a+b)
# elif oper == '*':
#     print(a*b)
# elif oper == '-':
#     print(a - b)
# elif oper == '/':
#     print(a / b)
# else:
#     print('enter valid info')

# n = int(input('введите необходимое количество первых чисел n: '))
# m = int(input('введите кратность m: '))
# k = int(input('введите нижний предел k: '))
#
# for i in range (k, (k + m * (n + 1))):
# #     if i % m == 0 and i != k:
# # #         print(i, end=' ')
#
# n = int(input('введите необходимое количество первых чисел n: '))
# m = int(input('введите кратность m: '))
# k = int(input('введите нижний предел k: '))
# while i > k:
#     if i % m == 0:
#         print(i)
#
# while i % m == 0:
#     if i > k:
#         print(i, end=' ')

n = int(input('input: '))
for i in range(2, (n+1)):
    if i % 2 == 0:
        print(i, end=' ')