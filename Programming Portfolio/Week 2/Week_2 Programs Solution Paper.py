# Q1
name = input('Hello, what is your name? ')
print('Hello, ', name, '. It is good to meet you!', sep='')


# Q2
celsius = float(input('Enter a temperature in Celsius: '))
print(celsius, 'C is equivalent to ', celsius * 1.8 + 32, 'F.', sep='')

# Q3

students = int(input('How many students? '))
group_size = int(input('Required group size? '))

full_groups = students // group_size
left_over = students % group_size

print('There will be', full_groups, 'groups with', left_over, 'students left over.')

# Q4
sweets = int(input('How many sweets in the tub? '))
pupils = int(input('How many pupils present today? '))

sweets_per_pupil = sweets // pupils
sweets_left_over = sweets % pupils

print('There will be', sweets_per_pupil, 'sweets for each pupil, with', sweets_left_over, 'sweets left over.')