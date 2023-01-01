# rock-paper-scissors

import random

choices = ["rock" , "paper", "scissors"]

computer = random.choice(choices)

player = False

while player == False:
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print("It's a tie! You both chose", player)
    elif player == "Rock":
        if computer == "scissors":
            print("You win!", player, "crushed", computer)
        else:
            print("You lost!", computer, "covered", player)
    elif player == "Paper":
        if computer == "rock":
            print("You win!", player, "covered", computer)
        else:
            print("You lost!", computer, "cut", player)
    elif player == "Scissors":
        if computer == "paper":
            print("You win!", player, "cut", computer)
        else:
            print("You lost!", computer, "crushed", player)
    else:
        print("Choose either Rock, Paper, or Scissors!")
    
player = False
computer = random.choice(choices)
