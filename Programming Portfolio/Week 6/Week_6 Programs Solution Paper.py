# Q1
def my_bin(i):
    return str(bin(i))[2:]

for x in range(32):
    print(f'{x} -> {my_bin(x)}')

# Q2
def factorise(num):
    return [f for f in range(1, num + 1) if num % f == 0]

for x in range(10, 25):
    print(f'{x} -> {factorise(x)}')

# Q3
from factors import factorise

def is_prime(i):
    return i > 1 and len(factorise(i)) == 2

for x in range(1, 101):
    print(f'{x:3} -> {"Prime" if is_prime(x) else "Not Prime"}')

# Q4
def obfuscate(message):
    letters = [c for c in message if c.isalpha()]
    letters.reverse()

    return ''.join(letters)

m = 'send cheese'

print(f'"{m}" -> "{obfuscate(m)}"')

# Q5
from string import ascii_lowercase as letters
from random import choice, randint

def random_letter():
    return choice(letters)

def n_random_letters(n):
    return ''.join([random_letter() for count in range(n)])

def encrypt(message):
    spacing = randint(2, 20)

    encrypted = ''

    for letter in message:
        encrypted += letter + n_random_letters(spacing)

    return encrypted, spacing

def decrypt(message, spacing):
    return message[::spacing + 1]

m = 'send cheese'

encrypted_message, spacing_used = encrypt(m)

print(f'"{m}" -> "{encrypted_message}", spacing {spacing_used}')
print(f'"{decrypt(encrypted_message, spacing_used)}"')


