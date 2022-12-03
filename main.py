# number = [1, 2, 3, 4]
# print(number[0])
# print(number[2])
# number[2] = 'python'
# print(number)
# print(number[2][1])
#
# print(len(number))
#
# letters = ['a', 'c', 'd', 'b']
# letters.sort(reverse=True)
# print(letters)
#
# letters = ['a', 'c', 'd', 'b']
# letters.sort(reverse=False)
# print(letters)

# number = (1, 2, 3, 4)
# print(number)
# number = list(number)
# print(number)
# number.append(5)
# numbers = tuple(number)
# print(numbers)

# text = input('Enter your text: ')
# list_text = list(text)
# print(list_text)
# text2 = [1, 2, 'a', 'b', 5]
# print(text2)
# print(list('hello'))
#
# text = [1, 2, 3, 'a', 'b']
# del text[1]
# el3 = text.pop(3)
# text.remove(1)
# print(text)
# print(el3)

# text = input('Please, enter degree "n": ')
# c = [c or c in range(1, n)]

# list_degree = [1, 2, 3, 4]
degree = input('Please, enter last degree: ')
degree = int(degree)
list_degree = [y for y in range(1, (degree + 1))]

new_list = [2**i for i in list_degree]
print(new_list)