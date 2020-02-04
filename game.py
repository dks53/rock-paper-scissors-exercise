# game.py

#print("Rock, Paper, Scissors, Shoot!!")

import random

print("--------------------------------------------")
print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME")
print("--------------------------------------------")

options = ["ROCK", "PAPER", "SCISSORS"]
user_choice = input("Please choose Rock or Paper or Scissors: ")
comp_choice = random.choice(options)

if user_choice.upper() in options:
    print("You chose: ", user_choice.upper())
    print("The computer chose: ", comp_choice)
    print("--------------------------------------------")

else:
    print("You entered an invalid input. Try again!")
    print("--------------------------------------------")
    exit()

if user_choice.upper() == "ROCK" and comp_choice == "SCISSORS":
    print("Niiicceeee!! You won!")
    print("--------------------------------------------")

elif user_choice.upper() == "SCISSORS" and comp_choice == "PAPER":
    print("Nailed it! You won!")
    print("--------------------------------------------")    

elif user_choice.upper() == "PAPER" and comp_choice == "ROCK":
    print("Genius!! You won!")
    print("--------------------------------------------")

elif comp_choice == "PAPER" and user_choice.upper() == "ROCK":
    print("Aww man! You lose! Better luck next time!")
    print("--------------------------------------------")

elif comp_choice == "SCISSORS" and user_choice.upper() == "PAPER":
    print("Bummer!! The computer beat you this team! Try again!")
    print("--------------------------------------------")

elif comp_choice == "PAPER" and user_choice.upper() == "ROCK":
    print("Yikes! You're out of luck :(")
    print("--------------------------------------------")

elif user_choice.upper() == comp_choice:
    print("There was a 33.3% chance you chose the same thing. It's a TIE!!!")
    print("--------------------------------------------")

else:
    print("Something's wrong with your code!")
    print("--------------------------------------------")



#comp_choice = 