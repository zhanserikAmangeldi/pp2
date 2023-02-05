import random

numberofguess = 0
random_num = random.randrange(1,20)

print("Hello! What is your name?")
name = input()

print(f"well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")


while True:
    numberofguess += 1
    numberofplayer = int(input())
    if random_num == numberofplayer:
        print(f'Good job, {name}! You guessed my number in {numberofguess} guesses!')
        break
    elif random_num > numberofplayer:
        print("Your guess is too low.\nTakes a guess.")
        continue
    elif random_num < numberofplayer:
        print("Your guess is too more.\nTakes a guess.")
        continue