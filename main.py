#task 1
# Choosing a random number

import random

random_num = random.randint(1,100)
guess = 1

while True:
    guess_num = int(input("Guess any number between 1-100: "))



    if guess_num == random_num:
        print("Congratulations, that is correct! ")
        print("Number of tries: ", guess)
        exit()


    elif guess_num > random_num:
        print("Your number was way too big, better luck next time!")
        guess = guess + 1


    elif guess_num < random_num:
        print("Your number is way to small, better luck next time!")
        guess = guess + 1









