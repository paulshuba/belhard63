# User enters a sentence, change all spaces with "-" symbol by 2 ways

# Way 1
sentence = input('Please, enter your sentence: ')
sentence = sentence.replace(' ', '-')
print(sentence)

# Way 2
sentence = input('Please, enter your sentence: ')
new_sentence = sentence.split(' ')
sentence = '-'.join(new_sentence)
print(sentence)