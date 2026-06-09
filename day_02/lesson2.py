# Day 2:30 Days of python programming

first_name = input('Please, enter your first name: ')
last_name = input('Please, enter your last name: ')
full_name = (first_name + ' ' + last_name)
country = input('Enter the country from where you are: ')
city = input('Please, enter the city wher you live: ')
age = input('How old are you: ')
birthdate = input('In what year were you born: ')
print('Welcome', full_name, 'of', city,',',country, ',to the second day of "30 days of Programming". Ive heard that you are',age, 'years old, and you were born in', birthdate, ', same as I!!.')
is_married = int(input('Are you married? Please, enter one option: \n1.True\n2.False\n'))

if is_married == 1:
    marriage = True
    couple_first_name = input('Please enter your couple name: ')
else:
    marriage = False
    couple_first_name = 'Its, ok not to have a couple.'
    print('There is no reason to be sad, there is plenty of fish in the sea.')

print('\nThank you for beeing here on these day, helping me to improve. I hope you are having a great day!')

print('Excercises: Level 2:')
print('1.',type(first_name),type(last_name),type(full_name), type(country), type(city), type(age), type(birthdate), type(is_married), type(marriage), type(couple_first_name))
print('2.', 'lenght first name: ',len(first_name))
print('3.', 'lenght last name: ', len(last_name))
num_one = int(input('Please enter a number: '))
num_two = int(input('Please enter a number: '))
total = 0
opt = 0
while opt == 0:
    opt = int(input('What operation would you like to do, please, select a number: ' \
                    '\n5. Addition' \
                    '\n6. Substraction' \
                    '\n7. Multiplication' \
                    '\n8. Divition' \
                    '\n9. Moudulus' \
                    '\n10. Exponential' \
                    '\n11. Floor division:'
                    '\n'))

    if opt == 5:
        total = num_one + num_two
    elif opt == 6:
        total = num_one - num_two
    elif opt == 7:
        total = num_one * num_two
    elif opt == 8:
        total = num_one / num_two
    elif opt == 9:
        total = num_one % num_two
    elif opt == 10:
        total = num_one ** num_two
    elif opt == 11:
        total = num_one // num_two
    else:
        opt = 0 
        print('Invalid Option.')

print('The result of your operation is: ', total)

radius = int(input('Please enter the radius of the circle: '))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print('The area of the circle is: ', area_of_circle, '\nAnd the circumference of the circle is: ', circum_of_circle)