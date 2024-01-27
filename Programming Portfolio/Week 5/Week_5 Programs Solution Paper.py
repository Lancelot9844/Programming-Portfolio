# Q1
from sys import platform


if __name__ == '__main__':
    print(f'This program is running under {platform.capitalize()}.')

# Q2
from sys import argv


if __name__ == '__main__':
    args = len(argv) - 1
    print(f'This program has {args} argument{"s" if args != 1 else ""}.')

# Q3
from sys import argv


if __name__ == '__main__':
    if len(argv) == 1:
        print('No CLAs provided. So none is the shortest.')
    elif len(argv) == 2:
        print(f'Just the one CLA, so it must be shortest: {argv[1]}.')
    else:
        sorted_args = argv[:]
        sorted_args.sort(key=len)
        print(f'Shorted argument (of the {len(argv) - 1}): {sorted_args[0]}.')

# Q4
from sys import argv
import urllib.request

HTTP_SUCCESS = 200

if __name__ == '__main__':
    try:
        code = urllib.request.urlopen(argv[1]).getcode()

        if code == HTTP_SUCCESS:
            print(f'Webpage at "{argv[1]}" looks OK.')
        else:
            print(f'No Webpage found at "{argv[1]}".')
    except IndexError:
        print('No URL on command-line. Nothing to do.')
    except:
        print('Something unexpected happened. Probably a DNS failure. Does the server exist?')

# Q5
# Alternate file for question 5
def chomp(s):
    return s[:-1] if len(s) > 1 else s


if __name__ == '__main__':
    for s in ['cheesey', '123456', 'Ni', 'spam', '', 'A']:
        print(f'"{s}" -> "{chomp(s)}"')

from statistics import mean
from sys import argv

from chomp import chomp


def read_temperatures(temp_list):
    temps = []

    for arg in temp_list:
        if arg.endswith(('C', 'c')):
            temps.append(float(chomp(arg)))
        else:
            raise ValueError('Invalid data on command-line')

    return temps


def print_results(temps_list):
    print()
    print(f'Max Temp:  {max(temps_list):6.2f}C.')
    print(f'Min Temp:  {min(temps_list):6.2f}C.')
    print(f'Mean Temp: {mean(temps_list):6.2f}C.')
    print()


if __name__ == '__main__':

    try:
        print_results(read_temperatures(argv[1:]))
    except ValueError:
        print('Error processing data. How sad.')

# Q6
from shutil import copyfile
from sys import argv
# In this program we musthave to run program using terminal & we can backup any file using terminal

if __name__ == '__main__':
    try:
        filename_in = argv[1]
        filename, extension = filename_in.split('.')

        filename_out = f'{filename}-backup.{extension}'

        copyfile(filename_in, filename_out)
    except IndexError:
        print('No filename supplied. Nothing to do.')
    except ValueError:
        print('Argument does not look like a filename. Cannot find file extension.')
    except FileNotFoundError:
        print(f'Cannot open "{filename_in}". Bailing out.')