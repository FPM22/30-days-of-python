# Exercises - Day 3
# Title
print('-'*50,' Exercises - Day 3 ' ,'-'*50 +'\n'+'-'*122)

# 1)
print('\n1)')
age = int(input('Please, enter your age: '))
height = float(input('Please, enter your height(Cm): '))
print('This person is', age, 'years old and is', height, 'cms tall.\n')

# Triangle Area
print('-'*122,'\n\n2)')
triangle_base = int(input('Please, enter the base of the triangle: '))
triangle_height = int(input('Please, enter the height of the triangle: '))
triangle_area = triangle_base * triangle_height / 2
print('The triangle area is: ', triangle_area, 'cm^2.\n')

# Triangle Perimeter
print('-'*122,'\n\n3)')
triangle_side_a = int(input('Please, enter side "a" of the triangle: '))
triangle_side_b = int(input('Please, enter side "b" of the triangle: '))
triangle_side_c = int(input('Please, enter side "c"  of the triangle: '))
triangle_perimeter = triangle_side_a + triangle_side_b + triangle_side_c
print('The triangle perimeter is: ', str(triangle_perimeter) + '.')

# Rectangle Area
print('-'*122,'\n\n4)')
rectangle_base = int(input('Please, enter the base of the rectangle: '))
rectangle_height = int(input('Please, enter the height of the rectangle: '))
rectangle_area = rectangle_base * rectangle_height
print('The rectangle area is: ', rectangle_area, 'cm^2.\n')

# Circle Area and Circumference
print('-'*122,'\n\n5)')
radius = float(input('Please, enter the radius of the circle: '))
circle_area = 3.14 * radius ** 2
circle_circumference = 2 * 3.14 * radius
print('The circle area is:', circle_area, 'cm^2, and the Circumference is:', circle_circumference,'\n')

# Slope, x-intercept, y-intercept
# a)
print('-'*122,'\n\n6)\n\na)')
m = int(input('Please, enter a number "m" for "mx" for the equation: '))
b = int(input('Please, enter a number "b" for "b" for the equation: '))
slope = m 
x_intercept = -b/m
y_intercept = b
print('The equation is:', str(m)+'x' , '+', str(b))
print('Slope =', slope, '| x_intercept = ', x_intercept, '| y_intercept =', y_intercept,'\n')

# b)
print('b)')
x1, y1 = 2, 2
x2, y2 = 6, 10 
slope2 = (y2-y1)/(x2-x1)
hypotenuse = ((y2-y1)**2+(x2-x1)**2)**(1/2)
print('The slope between point (2, 2) and point (6,10) is:', slope2)
print('The hypotenuse of the triangle formed by point (2, 2) and point (6,10) is:', hypotenuse, '\n')

# c)
print('c)')
if slope > slope2:
    print('Between slope:', slope,'and slope:', slope2, 'The greatest is:', slope, '\n')
elif slope < slope2:
    print('Between slope:', slope,'and slope:', slope2, 'The greatest is:', slope2, '\n')
else:
    print('They are the same. ', '\n')

# True or False
# a)
print('-'*122,'\n\n7)\n\na)')
lenght_comparison = len('python') != len('dragon')
print(lenght_comparison, '\n')

# b) 
print('b)')
on = 'on' in 'python' and 'on' in 'dragon'
print(on, '\n')

# c)
print('b)')
jargon = 'jargon' in 'I hope this course is not full of jargon' 
print(jargon, '\n')

# d)
string_python = str(float(len('python')))
print('The lenght of "python" is:', string_python)

# Even or Odd Number
print('-'*122,'\n\n8)\n\n')
number = int(input('Please enter any number: '))
if number % 2 == 0:
    print ('The number you have entered: ', number, 'is an even number.')
else:
    print('The number you have entered: ', number, 'is an odd number.')

# Weekly Payment
print('-'*122,'\n\n9)\n\n')
hours = int(input('Please, enter how many hours do you work a week: '))
rate_per_hour = int(input('Please, enter how much do you earn per hour: '))
print('You earn', '$'+str(hours*rate_per_hour), 'a week.')

# Number of seconds lived
print('-'*122,'\n\n10)\n\n')
years_lived = int(input('Please, enter how many years you lived: '))
print('You have lived:', years_lived*365*24*60*60, 'seconds.')

# Exponentials

print('-'*122,'\n\n11)\n\n')

v = int(input('Hasta que potencia quieres llegar?: '))

for i in range (5):
    for p in range(v+1):
        print(i**p, end=' ')
    print()
