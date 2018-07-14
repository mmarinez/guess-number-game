import random

print("-------------------")
print("  Guess Game Start")
print("-------------------")

number_to_guess = random.randint(0, 10)
player = -1

while (player != number_to_guess):
    player_number = input("Guess the number between 0 to 10:")
    player = int(player_number)

    if(player < number_to_guess):
        print("You number is lower than guess number, try again.")
    elif(player > number_to_guess):
        print("You number is higher than the guess number, try again")
    else:
        print("Winner chicken dinner!!")
