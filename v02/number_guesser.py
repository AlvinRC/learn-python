'''
Modify the number guesser from the video to print out the 
number of times guessed in total
'''

from random import randint

answer = randint(1, 10)
count_incorrect = 1

guess = int(input('Enter a guess between 1 and 10\n'))

while guess != answer:
    count_incorrect += 1

    if guess < answer:
        guess = int(input('Guess was too low!\n'))

    else:
        guess = int(input('Guess was too high!\n'))

print(f'You got the correct answer in {count_incorrect} guesses!')



# A variation using ternary operator (NOT recommended)

from random import randint

answer = randint(1, 10)
count_incorrect = 1

guess = int(input('Enter a guess between 1 and 10\n'))

while guess != answer:
    count_incorrect += 1

    msg = 'low' if guess < answer else 'high'
    guess = int(input(f'Guess was too {msg}!\n'))

print(f'You got the correct answer in {count_incorrect} guesses!')