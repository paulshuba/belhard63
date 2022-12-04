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
# degree = input('Please, enter last degree: ')
# degree = int(degree)
# list_degree = [y for y in range(1, (degree + 1))]
#
# new_list = [2**i for i in list_degree]
# print(new_list)

# list = [1, 2, 3, 4]
# print(2 in list)
# print(5 in list)
# print(6 not in list)
# print(2 not in list)
#
# list = [1, 2, 3, 4]
# list.append('new')
# print(list)

# list = [1, 2, 3, 4]
# list.insert(2, 'new')
# print(list)

# list = [1, 2, 3, 4]
# text = 'hello'
# list.extend(text)
# print(list)

# list = [1, 2, 3, 4, 2]
# print(list.index(2, 0, 5))
#
# list = [1, 2, 3, 4, 2]
# print(list.count(2))
#
# list = [1, 3, 5, 4, 2]
# list.sort()
# print(list)

# list = [1, 3, 5, 4, 2]
# print(sorted(list))
# print(list)
#
# list = [1, 3, 5, 4, 2]
# list.sort(reverse=True)
# print(list)
#
# list = [1, 3, 5, 4, 2]
# list.sort(reverse=False)
# print(list)

# list = [1, 3, 8, 7]
# list.reverse()
# print(list)

# list = [1, 2, 3, 4]
# list.clear()
# print(list)

# list = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = list + list2
# print(list3)

# list = [1, 2, 3, 4]
# tuple = tuple(list)
# print(tuple)

# tpl = (1, 2, 3, 4)
# tpl_list = list(tpl)
# tpl_list.append('new')
# print(tpl_list)
# tpl = tuple(tpl_list)
# print(tpl_list)

# tpl = (1, 2, 3, 4)
# new_set = set(tpl)
# print(new_set)

# start_set = 'text'
# new_set = {i for i in start_set}
# print(new_set)

# new_set = set('text')
# print(new_set)

# a = {i**2 for i in range(10)}
# print(a)

# set_1 = {1, 2, 3, 4}
# set_2 = {3, 5}
# set_3 = {5, 6}
# print(set_1.isdisjoint(set_2))
# print(set_1.isdisjoint(set_3))

# set_1 = {1, 2, 3, 4}
# set_2 = {3, 5}
# # set_1.intersection_update(set_2)
# # # print(set_1)
# #
# user1 = {
#     'name': 'Pavel',
#     'age': 34,
#     'city': 'Slutsk'
# }
# print(user1)
# user1['name'] = 'Anton'
# print(user1)
# print(user1['name'])
# print(user1.get('name'))
# print(user1.setdefault('name'))
# print(user1.setdefault('hobby', None))
# user1['sex'] = 'Male'
# print(user1)
# print(user1.keys())

# import collections
# text = input()
# data = collections.Counter(text)
# print(data)

text = input()
dict1 = {i:text.count(i) for i in text}

print(dict1)
