# Q1
def find_letters(string):
    return sorted(list(set(string)))

if __name__ == '__main__':

    for test_string in ['cheese', 'arthur', 'camelot', 'robin', 'a', '']:
        print(f'"{test_string}" -> "{find_letters(test_string)}"')

# Q2
def set_to_sorted_list(a_set):
    return sorted(list(a_set))

def find_all_letters(word_one, word_two):
    return set_to_sorted_list(set(word_one) | set(word_two))

def find_letters_in_both(word_one, word_two):
    return set_to_sorted_list(set(word_one) & set(word_two))

def find_letters_difference(word_one, word_two):
    return set_to_sorted_list(set(word_one) ^ set(word_two))

word = 'spam'
werd = 'eggs'

print(find_all_letters(word, werd))
print(find_letters_in_both(word, werd))
print(find_letters_difference(word, werd))

# Q3
capitals = {}

while True:
    country = input('Enter the name of a country: ')

    if not country:
        break

    if country.lower() in capitals:
        print(f'The capital of {country.capitalize()} is {capitals[country.lower()]}.')
    else:
        capital = input(f'Hmm. Please enter the capital of {country.capitalize()}: ')
        capitals[country.lower()] = capital.capitalize()

# Q4
from operator import itemgetter
from string import ascii_lowercase as letters

counts = {letter: 0 for letter in letters}

message = input('Enter the message: ')

for character in message.lower():
    if character in letters:
        counts[character] += 1

most_common = sorted(counts.items(), key=itemgetter(1), reverse=True)[:5]

for final_count in most_common:
    letter, count = final_count
    print(f'{letter} -> {count}')