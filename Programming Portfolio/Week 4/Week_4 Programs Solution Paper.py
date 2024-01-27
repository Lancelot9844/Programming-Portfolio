# Q1
def is_between_zero_and_hundred(an_integer):
    return 0 <= an_integer <= 100
for i in [-100, -50, -1, 0, 1, 25, 50, 75, 99, 100, 101, 125, 150, 1000]:
    print(f'{i:3} -> {is_between_zero_and_hundred(i)}')

# Q2
def count_letters(a_string):
    upper = lower = 0

    for letter in a_string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return lower, upper

for s in ['cheese', 'Cheese', 'CHEESE', 'ChEeSeY', 'cheeseIness', 'ch33se', '123456']:
    print(f'{s:12} -> Lower: {count_letters(s)[0]:2} Upper: {count_letters(s)[1]:2}')

# Q3
name = input('Hello, what is your name? ')
print(f'Hello, {name.capitalize() if name else "Stranger"}! It is good to meet you!')

# Q4
def chomp(s):
    return s[:-1] if len(s) > 1 else s

for s in ['cheesey', '123456', 'Ni', 'spam', '', 'A']:
    print(f'"{s}" -> "{chomp(s)}"')


# Q5
def c2f(c):
    return c * 9 / 5 + 32

def f2c(f):
    return (f - 32) * 5 / 9

for c in range (-20, 40, 5):
    print(f'{c:3}C -> {c2f(c):>6.2f}F')

    print()

    for f in range(20, 90, 5):
        print(f'{f:3}F -> {f2c(f):>6.2f}C')

            
# Q6
print("this is 6 question")

from temps import c2f
from chomp import chomp

if __name__ == '__main__':

    try:
        temp_c_str = input('Enter a Centigrade Temperate (end it with C): ')

        if temp_c_str.endswith(('C', 'c')):
            temp_f = c2f(float(chomp(temp_c_str)))
            print(f'{temp_c_str.upper()} is equivalent to {temp_f:.2f}F.')
        else:
            print('No "C" at the end of the input. Why not try again?')
    except ValueError:
        print('Invalid input. Why not try again?')

# Q7
from statistics import mean

from chomp import chomp

NUMBER_OF_TEMPS = 6


def read_temperatures(number_of_temps=NUMBER_OF_TEMPS):
    temps = []

    while len(temps) < number_of_temps:
        try:
            temp_c_str = input('Enter a Centigrade Temperate (end it with C): ')

            if temp_c_str.endswith(('C', 'c')):
                temps.append(float(chomp(temp_c_str)))
            else:
                print('No "C" at the end of the input. Why not try again?')
        except ValueError:
            print('Invalid input. Why not try again?')

    return temps

def print_results(temps_list):
    print()
    print(f'Max Temp:  {max(temps_list):6.2f}C.')
    print(f'Min Temp:  {min(temps_list):6.2f}C.')
    print(f'Mean Temp: {mean(temps_list):6.2f}C.')
    print()


if __name__ == '__main__':

    print_results(read_temperatures(NUMBER_OF_TEMPS))

# Q8
from statistics import mean

from chomp import chomp


def read_temperatures():
    temps = []

    while True:
        try:
            temp_c_str = input('Enter a Centigrade Temperate (end it with C): ')
            if not temp_c_str:
                break

            if temp_c_str.endswith(('C', 'c')):
                temps.append(float(chomp(temp_c_str)))
            else:
                print('No "C" at the end of the input. Why not try again?')
        except ValueError:
            print('Invalid input. Why not try again?')

    return temps

def print_results(temps_list):
    print()
    print(f'Max Temp:  {max(temps_list):6.2f}C.')
    print(f'Min Temp:  {min(temps_list):6.2f}C.')
    print(f'Mean Temp: {mean(temps_list):6.2f}C.')
    print()

if __name__ == '__main__':

    try:
        print_results(read_temperatures())
    except ValueError:
        print('No data entered. Nothing to do. How sad.')