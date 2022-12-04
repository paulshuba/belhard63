# Create dictionary with keys from 0 to N, and values as dictionaries with keys 'name' and 'e-mail'
# and values, entered from keyboard.

n = input('Enter N: ')
n = int(n)
dict1 = {i:{'name': input('Enter name: '), 'e-mail': input('Enter e-mail:')} for i in range((n+1))}
print(dict1)