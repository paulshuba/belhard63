n = int(input("Enter quantity of first numbers 'n': "))
m = int(input("Enter multiplicity 'm': "))
k = int(input("Enter lower range 'k': "))

# for i in range (k, (k + (m * (n + 1)))):
#     if i % m == 0 and i > k:
#         print(i, end=' ')

count = 0
while count < k:
    print(count)
    count += 1
    # print(count)
    # if count > 5:
    #     break
