'''
# Exercises - Day 4
# Title
print('\n'+'-'*50,' Exercises - Day 5 ' ,'-'*50 +'\n'+'-'*122)

# List: Is a collection which is ordered and changeable. Allows duplicate members

#1 

empty_list = []

lst = ['element1','element2','element3','element4','element5']

print(len(lst))

print(lst[0])

name = input('Name: ')
age = input('Age: ')
height = input('Height: ')
marit_stat = input('Marital Status: ')
adress = input('Adress: ')
mixed_data_types = [name, age, height, marit_stat, adress]

print(mixed_data_types)

companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(companies)
print(len(companies))
print(companies[0])
print(companies[-1])
print(companies[(len(companies)//2)])
companies[2] = 'Nvidia'
print(companies)
companies.append('Vercel')
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.insert(len(companies)//2, 'Kingston')
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
string = ['#; ']
companies.extend(string)
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
does_exists = 'Vercel' in companies
print(does_exists)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.sort()
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.reverse()
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del companies[0:3]
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del companies[-3:]
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del companies[-(len(companies)//2):]
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.pop(0)
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.pop((len(companies)//2))
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
companies.pop(-1)
print(companies)
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del companies[0:]
print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
print(full_stack)'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = ages[0]
max_age = -1
for i in range(len(ages)):
    if ages[i] < min_age:
        min_age = ages[i]
    else:
        min_age = min_age
    if ages[i] > max_age:
        max_age = ages[i]
    else:
        max_age = max_age

print('min age:',min_age)
print('max_age:',max_age)