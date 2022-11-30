# User enters Name, Age and City, form hello-message by 3 ways.

# Way 1
name = input('Please, enter your name: ')
age = input('Please, enter your age: ')
city = input('Please, enter your city: ')
print(f"Hello!\nMy name is {name}.\nI'm {age} years old.\nMy native city is {city}.\n")


# Way 2
name = input('Please, enter your name: ')
age = input('Please, enter your age: ')
city = input('Please, enter your city: ')
print("Hello!\nMy name is {}.\nI'm {} years old.\nMy native city is {}.\n".format(name, age, city))


# Way 3
name = input('Please, enter your name: ')
age = input('Please, enter your age: ')
city = input('Please, enter your city: ')
print('Hello!\nMy name is %s.\nI\'m %s years old.\nMy native city is %s.\n' % (name, age, city))


# + Way 4
name = input('Please, enter your name: ')
age = input('Please, enter your age: ')
city = input('Please, enter your city: ')
print('Hello!\nMy name is ' + name + "\nI'm " + age + ' years old.' +'\nMy native city is ' + city + '.\n')