import json

import random
import os
import time as t

clear = lambda: os.system("cls")
clear()

wins = 0
losses = 0
ties = 0

usertally = 'usertally.json'

name = input("What will your username be for your sessions?\n")

user_wlt_dic =  {
    "name":name, 
    "WLT": {
        "wins": 0, 
        "losses": 0,
        "ties": 0
    }
}

with open(usertally, "r") as file:
    data_dic = json.load(file)

data_dic["data"].append(user_wlt_dic)

if data_dic["data"].count(name) != 0:
    data_dic["data"]["name"] = name 
    data_dic["data"]["WLT"]["wins"] = wins
    data_dic["data"]["WLT"]["losses"] = losses
    data_dic["data"]["WLT"]["ties"] = ties

else:
    data_dic["data"]["name"] = name


def c_choice():
    computer_move = random.randint(0, 2)
    if computer_move == 0:
        computer_move = "rock"
    elif computer_move == 1:
        computer_move = "scissors"
    elif computer_move == 2:
        computer_move = "paper"
    return computer_move

def victory(comp_move, player_move):
    wins = 0
    losses = 0
    ties = 0
    if player_move != "rock" and player_move != "paper" and player_move != "scissors":
        print("You did not choose a valid move. Please retry.")
    elif comp_move == "rock" and player_move == "rock":
        print("It's a tie. Whoops!")
        ties += 1
    elif comp_move == "rock" and player_move == "paper":
        print("Looks like you won! Congratulations!")
        wins += 1
    elif comp_move == "rock" and player_move == "scissors":
        print("Uh oh...you lost. Try another move.")
        losses += 1
    elif comp_move == "scissors" and player_move == "scissors":
        print("It's a tie. Whoops!")
        ties += 1
    elif comp_move == "scissors" and player_move == "paper":
        print("Uh oh...you lost. Try another move.")
        losses += 1
    elif comp_move == "scissors" and player_move == "rock":
        print("Looks like you won! Congratulations!")
        wins += 1
    elif comp_move == "paper" and player_move == "rock":
        print("Uh oh...you lost. Try another move.")
        losses += 1
    elif comp_move == "paper" and player_move == "scissors":
        print("Looks like you won! Congratulations!")
        wins += 1
    elif comp_move == "paper" and player_move == "paper":
        print("It's a tie. Whoops!")
        ties += 1
    return wins, ties, losses
        
    

def validity():
    if player_move == "rock" or player_move == "paper" or player_move == "scissors":
        print(f"You chose {player_move}!")
    else:
        print("\nWait, what?")
        t.sleep(1)
        print("You chose...")
        t.sleep(1)
        print(player_move.capitalize() + "?")
    if player_move == "rock" or player_move == "paper" or player_move == "scissors":
        print("\nThe computer is choosing...")
        t.sleep(2)
        print(f"The computer chose {comp_move}!")
    else:
        t.sleep(1)
        print("\nThe computer is disappointed in you.")
    


while True:
    player_move = input("--- What move are you going with? Please input your answer as rock, paper, or scissors. ---\nYour choice: ") 
    comp_move = c_choice()
    validity()
    victory(comp_move, player_move) 
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print("\n")
    
    

    exit_cmd = input("--- Do you wish to exit the game? ---\ny/n: ")
    if exit_cmd == "y":
        quit(1)
    elif exit_cmd == "n":
        print("\nAlright, play as long as you'd like!\n")
    else:
        print("\nYou did not input a valid command so the game will continue.\n")



#exit when done
#play against someone else
#tally of wins, losses, and ties
    #intermediate - ask for username, associate wins, losses, and ties to that
        






    

