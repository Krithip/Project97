import random
number = random.randint(1, 10)
chances = 3
print("guess a number between 1 to 10")
while chances>0:
    guess = int(input("enter your guess"))
    if(guess == number):
        print("Congratulations! You guessed correctly!")
        break
    elif guess<number:
        print("Your guess was wrong. Guess a higher number")
    else:
        print("Your guess was wrong. Guess a lower number")
    chances = chances - 1
if chances == 0:
    print("You lose")