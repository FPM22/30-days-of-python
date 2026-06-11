# Exercises - Day 4
# Title
print('\n'+'-'*50,' Exercises - Day 4 ' ,'-'*50 +'\n'+'-'*122)

# 1)
print('\n1)')
sentence = ['Thirty', 'Days', 'Of', 'Python'] 
thirtydaysofpython = ' '.join(sentence)
print(thirtydaysofpython)
print('')

# 2)
print('-'*122,'\n\n2)')
sentence2 = ['Coding', 'For', 'All']
codingforall = ' '.join(sentence2)
print(codingforall)
print('The lenght of the sentence is:',str(len(codingforall))+'.')
print('Sentence in uppercase letters:',codingforall.upper())
print('Sentence in lowercase letters:',codingforall.lower())
print('Sentence capitalized:', codingforall.capitalize())
print('Sentence titled:', codingforall.title())
print('Sentence swapcased: ', codingforall.swapcase())
print('') 
print('Sentence sliced:', codingforall[0:6])
print(codingforall.count('Coding'))
print(codingforall.replace('Coding', 'Python'))
print('Python For Everyone'.replace('Everyone', 'All'))
print(codingforall.split(' '))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
print(codingforall[0])

# 4)
