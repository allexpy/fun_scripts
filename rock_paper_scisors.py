"""In this program we will create a Rock Paper Scissors game."""

from random import randint
from time import sleep

option = ["R", "P", "S"]
PLAYER_LOST = "You lost..."
PLAYER_WIN = "Great, you won!"

def decide_winner(user_choice, computer_choice):
  print "You selected %s" % (user_choice)
  print "Computer selecting..."
  sleep(2)
  print "Computer chose %s" % (computer_choice)
  
  user_choice_index = option.index(user_choice) #user's index
  computer_choice_index = option.index(computer_choice) #computer's index    
  
  #Scenarios in which user wins.
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  
  elif user_choice_index == 0 and computer_choice_index == 2:
    print PLAYER_WIN
  
  elif user_choice_index == 1 and computer_choice_index == 0:
    print PLAYER_WIN
  
  elif user_choice_index == 2 and computer_choice_index == 1:
    print PLAYER_WIN
  
  elif user_choice_index > 2:
    print "An invalid option was selected!"
    return
  
  else:
    print "Computer won!"
    
def play_RPS():
  print "You are playing Rock, Paper, Scissors!"
  user_choice = raw_input("Select R for Rock, P for Paper or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = option[randint(0, len(option)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()
