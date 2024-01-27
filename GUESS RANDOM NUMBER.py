import random

while True:
        
    fix = random.randint(1,9)

    i = 1

    while i<=3:

        guess = int(input('Guess a number between 1 & 9: '))

        if guess == fix:

            print('You won the Game')

        else:
            print('Your guess is wrong')

        i =  i + 1

    else:
        print('You lost the game ')


    ch = input('Do you want to play again (yes/no): ')
    if ch == 'no':
        break

print('GAME OVER')
