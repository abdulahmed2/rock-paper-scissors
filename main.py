# rock-paper-scissors

import random

choices = ["Rock" , "Paper", "Scissors"]

computer = random.choice(choices)

player = False

while player == False:
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print("It's a tie! You both chose", player)
    elif player == "Rock":
        if computer == "Scissors":
            print("You win!", player, "crushed", computer)
        else:
            print("You lost!", computer, "covered", player)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost!", computer, "cut", player)
        else:
            print("You win!", player, "covered", computer)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!", player, "cut", computer)
        else:
            print("You lost!", computer, "crushed", player)
    else:
        print("Choose either Rock, Paper, or Scissors!")
for i in range(100):   
    player = False
    computer = random.choice(choices)
    while player == False:
        player = input("Rock, Paper, or Scissors?")
        if player == computer:
            print("It's a tie! You both chose", player)
        elif player == "Rock":
            if computer == "Scissors":
                print("You win!", player, "crushed", computer)
            else:
                print("You lost!", computer, "covered", player)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lost!", computer, "cut", player)
            else:
                print("You win!", player, "covered", computer)
        elif player == "Scissors":
            if computer == "Paper":
                print("You win!", player, "cut", computer)
            else:
                print("You lost!", computer, "crushed", player)
        else:
            print("Choose either Rock, Paper, or Scissors!")
