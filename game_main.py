import random

print("-------------------")
print("  Guess Game Start")
print("-------------------")

number_to_guess = random.randint(0,10)

player_number = input("Guess the number between 0 to 10\n")

player = int(player_number)
