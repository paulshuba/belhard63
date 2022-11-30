# User enters 3 numbers, find how many of them are plus and how many - minus.
first_number = input('Please, input your first number: ')
second_number = input('Please, input your second number: ')
third_number = input('Please, input your third number: ')
first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)
print('The quantity of plus numbers is: ', ((first_number > 0) + (second_number > 0) + (third_number > 0)))
print('The quantity of minus numbers is: ', ((first_number < 0) + (second_number < 0) + (third_number < 0)))
