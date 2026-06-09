# Day 2:30 Days of python programming

first_name = input('Please, enter your first name: ')
last_name = input('Please, enter your last name: ')
full_name = (first_name + ' ' + last_name)
print('Welcome', full_name + ',', 'to the second day of "30 days of Programming"')
country = input('Enter the country from where you are: ')
city = input('Please, enter the city wher you live: ')
age = input('How old are you: ')
birthdate = input('In what year were you born: ')
is_married = int(input('Are you married? Please, enter one option: \n1.True,\n2.False\n'))

if is_married == 1:
    marriage = True
    couple_first_name = input('Please enter your wifes name: ')
else:
    marriage = False
    print('There is no reason to be sad, there is plenty of fish in the sea.')

print('\nThank you for beeing here on these day, helping me to improve. I hope you are having a great day!')

print(type(marriage))