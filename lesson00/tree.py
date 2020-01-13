height = int(input('Enter tree\'s height: '))
for i in range(0, height):
    print(' ' * (height - i) + '*' * (i * 2 + 1))