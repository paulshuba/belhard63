# User enters 3 numbers, find average with an accuracy of 3 numbers.
first_number = input('Please, input your first number: ')
second_number = input('Please, input your second number: ')
third_number = input('Please, input your third number: ')
average = (int(first_number) + int(second_number) + int(third_number)) / 3
print('Average value is: ', round(average, 3))