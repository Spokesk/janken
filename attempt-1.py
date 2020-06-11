"""
    Janken (Rock, Paper, Scissors) Game. Four major parts: One ,prompt player
    for input, either Rock, Paper, or Scissors. Two, generate a random value for the computer
    (not sure how to do this with out building a dictionary.... inbuilt dictionary?
    should probabbly search...). Three, comapre inputted value with generated value
    decide (don't know how :/ ) whether there is a lose, win (for the user) or a tie.
    Four, prompt player if they want to play again.
"""

# Make random work
from random import choice

def start():
    # Define own possaability string
    jankenChoice = ['Rock', 'Paper', 'Scissors']

    # Have computer generate random variable from jankenChoice string
    computerChoice = choice(jankenChoice)

    # Specify exclusion criteria for userChoice
    while True:
        # Inform user of game
        # Prompt them to input a varible of 'rock', 'paper','scissors'.
        userChoice = input("kk kids, leeeeeet's plaaaaay JANKEN! Choose Rock, Paper, or Scissors! ").lower().capitalize()

        if userChoice == 'Rock' or userChoice == 'Paper' or userChoice == 'Scissors':
            break
        else: 
            print("Nooooooo play the game sport, choose an actual choice champ.")

   # Compare userChoice to computerChoice, use elif statements to negotiate outcome formula inform user of result
    # Inform user of result
def play()
    while True:
     if (
        computerChoice == 'Rock' and userChoice == 'Paper'
    ) or (
        computerChoice == 'Paper' and userChoice == 'Scissors'
    ) or (
        computerChoice == 'Scissors' and userChoice == 'Rock'
    ):
        print(computerChoice)
        print("Oof, nice one slugger, you got me beat!")
        break

    elif (
        computerChoice == 'Rock' and userChoice == 'Scissors'
    ) or (
        computerChoice == 'Paper' and userChoice == 'Rock'
    ) or (
        computerChoice == 'Scissors' and userChoice == 'Paper'
    ):
        print(computerChoice)
        print("I win skipper ;)")
        break

    else:
        print(computerChoice)
        print(":O a draw?! The scandle of it all!")
        break 

    # Prompt user to play again
    while True:
        promptAnswer = input("Wanna take another shot scamp? Yes/No ").lower().capitalize()
            
        if promptAnswer == 'Yes':
            start()
        elif promptAnswer == 'No':
            print("kk seeya babes :3")
            break
        else:
            print("Now now, answer propperly ol' chap.")

start()
play()
        