# Create dictionary which counts 'i' without using collections.
text = input('Enter your text: ')
dict1 = {i:text.count(i) for i in text}

print(dict1)
