import random

playAgain = 'yes'
while playAgain == 'yes':
    count = 1
    print('Welcome to the guessing game!')
    print()

    print('I am thinking of a number between 1 and 100.')
    secretNum = random.randint(1, 100)

    print('Take a guess')
    guess = int(input())

    while secretNum != guess:
        count = count + 1
        if guess < secretNum:
            print('Too low!')
        if guess > secretNum:
            print('Too high!')
        guess = int(input())

    print()
    print('That is correct!')
    print()
    print('It took you ' + str(count) + ' tries to get the right answer')
    print()
    print('Would you like to play again')
    playAgain = input()


