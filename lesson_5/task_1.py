n = int(input("Enter quantity of first numbers 'n': "))
m = int(input("Enter multiplicity 'm': "))
k = int(input("Enter lower range 'k': "))

numbers = []
while len(numbers) < n:
    if not k % m:
        numbers.append(k)
        k += m
    else:
        k += 1
print(numbers)