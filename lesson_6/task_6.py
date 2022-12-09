# Дан список рандомных чисел, необходимо отсортировать его в виде,
# сначала четные, потом нечётные.

import random
lst = []
lower_range = int(input('Enter lower range: '))
upper_range = int(input('Enter upper range: '))
lst_length = int(input('Enter length of the list: '))

for i in range(lst_length):
    lst.append(random.randint(lower_range, upper_range))
print(lst)

lst_a = [i for i in range(1, len(lst)) if i % 2 == 0]
lst_a.sort()

lst_b = [i for i in range(1, len(lst)) if not i % 2 == 0]
lst_b.sort()

print(lst_a + lst_b)
