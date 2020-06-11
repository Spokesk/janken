"""
  https://www.learnpython.org/en/Functions
  https://www.learnpython.org/en/Dictionaries
  https://codereview.stackexchange.com/questions/172337/rock-paper-scissors-game-in-python
"""

import sys
from random import randint


# Example of function inside function
def func1(): 
    def func2():
        return print("Function 2")
    
    return print("Function 1 is returning: ", func2())

def compare(playerChoice, cpuChoice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[(playerChoice, cpuChoice)]

def play():
  p_choice = input("What do you choose?").lower().capitalize()
  choices = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}
  cpu_choice = choices[randint(1,3)]

  if p_choice == cpu_choice:
      return print('Tie!')
  if compare(p_choice, cpu_choice):
      return print('You Win!')
  else:
      return print('You Lose!')

def game_start():
    begin = input("Would you like to play Rock, Paper, Scissors? Yes/No ").lower().capitalize()

    while begin != "Yes":
      if begin == "No":
          print("Game Over")
          sys.exit()
      else:
          print("Please try again")
          begin = input("Would you like to play Rock, Paper, Scissors? Yes/No ").lower().capitalize()

    play()

    while True:
        begin = input("Play again? ").lower().capitalize()

        while begin != "Yes":
            if begin == "No":
                print("Game Over")
                sys.exit()
            else:
                print("Please try again")
                begin = input("Play again? ").lower().capitalize()
        play()

game_start()