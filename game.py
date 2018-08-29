import random


num = random.randint(1,101)
guess = 0
print('Welcome to the HI - LO game')
while guess != num:
    guess = int(input('Guess a number between 1 & 100: '))
    if num == guess:
        print('Got it: The number is {}'.format(num))
    elif num > guess:
        print('Too low!')
    else:
        print('Too high!')

