"""
    Slighty expended choice game. I'm essentially upscaling my janken game
    do use the four classical elements. More possabilities and more outcomes
    my time to jive with funtions within functions and databases.

    By: The Woke-Up-On-The-Wrong-Side-This-Morning Kesk
"""
# First the database, defines the winning and loseing conditions, NOT the new multitude of getting a tie

from random import choice
import sys


# elements = {1 : 'Fire', 2 : 'Water', 3 : 'Air', 4 : 'Earth'}
elements = ['Fire', 'Water', 'Air', 'Earth']


def compare_win(comChoice, userChoice):
    outcomesWin = {('Fire', 'Water') : True,
                ('Water', 'Fire') : False,
                ('Air', 'Fire') : True,
                ('Fire', 'Air') : False,
                ('Earth', 'Air') : True,
                ('Air', 'Earth') : False,
                ('Water', 'Earth') : True,
                ('Earth', 'Water') : False}
    return outcomesWin[(comChoice, userChoice)] # returns True or False

def compare_tie(comChoice, userChoice):
    outcomesTie = {('Fire', 'Earth') : True,
                ('Earth', 'Fire') : True,
                ('Water', 'Air') : True,
                ('Air', 'Water') : True}
    return outcomesTie[(comChoice, userChoice)]            
    # unsure with how to sepcify which database to return with, it would need to be the one that has the 
    # outcome in it. Might need to merge them if to convoluted. They are as they are now as it will allow
    # to return certain text after certain outcomes

def playAgain():
    playerAnswer = input("Do you wanna shoot your load again son? ").lower().capitalize()
    
    if playerAnswer == "Yes":
        print("Kk heeeeere we go again :::DDD")
        return True
    elif playerAnswer == "No":
        print("See ya Spacecowboy!")
        return False
    else: 
        print("Let's try that again now!")
        return playAgain()

# Starting function, will cover the first half of the game, the choosing of elements and the outputted win or lose
def begin():
    # TODO fix this syntax mess, what do you want from me console?!
    print("Let's play Elemental Janken!
           The rules are:
           Water > Fire
           Fire > Air
           Air > Earth
           Earth > Water

           Any other combo and we'll try again!"):
   

    comChoice = choice(elements)
    userChoice = input("Kk Avatar, choose an element! ").lower().capitalize()

    print(comChoice, userChoice)

    try:
        if compare_win(comChoice, userChoice):
            print("Better luck next time champ")
    except: pass

    try:
        if compare_tie(comChoice, userChoice):
            print("Our powers are to diverse to assure victory!")
    except: pass

    
    if comChoice == userChoice:
        print("Mutual negation!")
    else:
        print("You win sunshine ;D")

    if playAgain():
    
    else:
         print("Smell you later alligator!")
        sys.exit
   
begin()
