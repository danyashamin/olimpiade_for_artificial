from random import randint

needInt = randint(1, 999)
playerInt = int(input('Угадай число:'))
while playerInt != needInt:
    if playerInt > needInt:
        print('меньше')
    else:
        print('больше')
    playerInt = int(input())
print('угадано')