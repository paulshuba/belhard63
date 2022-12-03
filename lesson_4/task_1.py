# Get list with "2" in degree from 1 to N.

degree = input('Enter last degree N: ')
degree = int(degree)
list_degree = [y for y in range(1, (degree + 1))]
new_list = [2**i for i in list_degree]
print(new_list)