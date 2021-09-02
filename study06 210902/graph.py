import sys

numbers = list(filter(lambda x: x.isdigit(), sys.argv[1]))
width = len(numbers)
height = int(max(numbers))
row = height

for j in range(height):
    for i in range(width):
        if int(numbers[i]) >= row:
            sys.stdout.write('* ')
        else:
            sys.stdout.write('  ')
    row -= 1
    sys.stdout.write('\n')

for number in numbers:
    sys.stdout.write(number + ' ')

sys.stdout.write('\n')