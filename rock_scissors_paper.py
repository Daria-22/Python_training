import random
import os
import time
from datetime import date
from datetime import datetime


#print(os.getcwd())

class HumanPlayer:
    def get_user_choice(self):
        valid_choices = ["rock", "scissors", "paper"]
        user_choice = input("Select and enter your choice from: rock, scissors, paper: ").lower()
        while user_choice not in valid_choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Select and enter your choice from: rock, scissors, paper: ").lower()
        return user_choice

class ComputerPlayer:
    def get_computer_choice(self):
        valid_choices = ["rock", "scissors", "paper"]
        return random.choice(valid_choices)

def determine_winner(human, computer):
    if human == computer:
        return "It's a draw! Both human and computer are winners!"
    elif (human == 'rock' and computer == 'paper'):
        return 'Computer wins, human loses as paper covers the rock!'
    elif (human == 'rock' and computer == 'scissors'):
        return 'Human wins, as rock breaks the scissors!'
    elif (human == 'paper' and computer == 'rock'):
        return "Human wins as paper covers the rock!"
    elif (human == 'paper' and computer == 'scissors'):
        return 'Computer wins as scissors cut the paper'
    elif (human == 'scissors' and computer == 'rock'):
        return 'Computer wins as rock breaks the scissors'
    elif (human == 'scissors' and computer == 'paper'):
        return 'Human wins as scissors cut the paper'
def play_game():
    humanPlayer = HumanPlayer()
    human = humanPlayer.get_user_choice()
    computerPlayer = ComputerPlayer()
    computer = computerPlayer.get_computer_choice()
    today = date.today()
    now = datetime.now()
    day_game = today.strftime("%d/%m/%Y")
    time_game =now.strftime("%H:%M:%S")
    print("Human player selected:")
    print(human)
    print("Computer player selected:")
    print(computer)
    winner = determine_winner(human, computer)
    print(winner)

    rps_game_res = open('Rock_paper_result.txt', 'a+')
    rps_game_res.write(day_game)
    rps_game_res.write(' ')
    rps_game_res.write(time_game)
    rps_game_res.write(' ')
    rps_game_res.write(winner)
    rps_game_res.write('\n')
    rps_game_res.close()


    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    if play_again == "yes" or play_again == "ye" or play_again == "y":
        play_game()
    else:
        print('\n It was a pleasure to play with you, human! Here are the results of the last games, including the current one \n')
        

def game1():
    print('Welcome to the game "Rock, scissors, paper"')
def read_result_from_file ():
    rps = open('Rock_paper_result.txt', 'r')
    print(rps.read())
    rps.close()

# Call the welcome screen
game1()
# Call the game logic
play_game()
# display the saved result
read_result_from_file ()




