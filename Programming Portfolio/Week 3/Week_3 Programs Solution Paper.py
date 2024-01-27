# Q1
name = input('Hello, what is your name? ')
print(f'Hello, {name if name else "Stranger"}! It is good to meet you!')

# Q2
password = input('Enter your new password:   ')
check = input('Re-enter the same password:')

if password == check:
    print('Password Set')
else:
    print('1Error. Passwords do not match.')

# Q3
password = input('Enter your new password:   ')
check = input('Re-enter the same password:')

if password == check and len(password) >= 8 and len(password) <= 12:
    print('Password Set')
else:
    print('2Error. Passwords do not match.')

# Q4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input('Enter your new password:   ')
check = input('Re-enter the same password:')

if password == check and len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS:
    print('Password Set')
else:
    print('3Error. Passwords do not match.')


# Q5
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password = input('Enter your new password:   ')
    check = input('Re-enter the same password:')
    if password == check and len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS:
        print('Password Set')
        break
    else:
        print('4Error. Passwords do not match.')


# Q6
for row in range(13):
    print(f'{row:2} x 7 = {row * 7:2}')

# 7
while True:
    table = int(input('What times table do you want to see? '))
    if 0 <= table <= 12:
        for row in range(13):
            print(f'{row:2} x {table} = {row * table:3}')
        break
    else:
        print('Sorry. That value is out of range. Try again.')

# Q8
while True:
    table = int(input('What times table do you want to see? '))

    if 0 <= abs(table) <= 12:
        if table >= 0:
            for row in range(13):
                print(f'{row:2} x {table} = {row * table:3}')
        else:
            for row in range(12, -1, -1):
                print(f'{row:2} x {abs(table)} = {row * abs(table):3}')
        break
    else:
        print('Sorry. That value is out of range. Try again.')