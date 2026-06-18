ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_age = ages[0]
max_age = -1

for age in ages:
    if age < min_age:
        min_age = age
    if age > max_age:
        max_age = age
    

print('min age:',min_age)
print('max_age:',max_age)

ages.sort()

ageselected = int(input('Age: '))

low = 0
high = len(ages) - 1
mid = (low + high) // 2

while low <= high:
    if ages[mid] < ageselected:
        low = mid + 1
    elif ages[mid] >= ageselected:
        high = mid - 1
    mid = (low + high) // 2

ages.insert(low, ageselected)
print(ages)

avg_ages = 0
for age in ages:
    avg_ages += age
avg_ages = avg_ages / len(ages)

print('The avarge age: ', avg_ages)      
max_ages = max(ages)          
min_ages = min(ages)
print('max:', max_ages, 'min:', min_ages)

age_distance = abs((min_ages - avg_ages) - (max_ages - avg_ages))
print('The distance between max and min age:', age_distance)
