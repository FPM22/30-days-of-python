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
print(codingforall,'\n')
print('The lenght of the sentence is:',str(len(codingforall))+'.\n')
print('Sentence in uppercase letters:',codingforall.upper(),'\n')
print('Sentence in lowercase letters:',codingforall.lower(),'\n')
print('Sentence capitalized:', codingforall.capitalize(),'\n')
print('Sentence titled:', codingforall.title(),'\n')
print('Sentence swapcased: ', codingforall.swapcase(),'\n')
print('Sentence sliced:', codingforall[0:6],'\n')
print(codingforall.count('Coding'),'\n')
print(codingforall.replace('Coding', 'Python'),'\n')
print('Python For Everyone'.replace('Everyone', 'All'),'\n')
print(codingforall.split(' '),'\n')
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','),'\n')
print(codingforall[0],'\n')
print(codingforall[-1],'\n')
print(codingforall.index('C'),'\n')
print(codingforall.index('F'),'\n')
print(codingforall.rindex('i'),'\n')
print('You cannot end a sentence with because because because is a conjunction'.index('because'),'\n')
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'),'\n')
print('You cannot end a sentence with because because because is a conjunction'[31:54],'\n')
print('You cannot end a sentence with because because because is a conjunction'.find('because'),'\n')
if codingforall.find('Coding') == 0:
    print(codingforall,'starts with \'Coding\'','\n')
else:
    print(codingforall, 'doesn\'t start with \'Coding\'','\n')
    