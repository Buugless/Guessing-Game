import random
import math
range_x = int(input("Give first positive  number in range: "))
range_y = int(input("Give second positive number in range: "))

if range_x <= 0 or range_y < 0:
    raise Exception("Range must be positive integer")
if range_y < range_x:
    raise Exception("Second number must be bigger then the first one")

random_number = random.randint(range_x,range_y)

minimum_number_of_gueses=math.ceil(math.log2(range_y-range_x+1))
print(f"You've only have {minimum_number_of_gueses} chances. Good luck!")

guess=-1
count = 1

while guess != random_number:
    minimum_number_of_gueses -= 1 
    guess = int(input("What's your guess: "))

    if guess < random_number:
        print("Try Again! You guessed too small ")
        count += 1
    elif guess > random_number:
        print("Try Again! You guessed too high ")
        count += 1
    if minimum_number_of_gueses == 0:
        print(f"The number is {random_number}")
        print("Better Luck Next Time")
        break
   
   
if guess == random_number:
    print(f"You guessed right! The correct number was {random_number} and number of guesses was: {count}")