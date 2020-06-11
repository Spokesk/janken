from random import choice

game_choices = ['Rock', 'Paper', 'Scissors']


def prompt_player():
    p_choice = input(
        "What do you choose Rock, Paper, or Scissors? ").lower().capitalize()

    if p_choice not in game_choices:
        print("You did not specify a choice. Choose Rock, Paper, or Scissors. ")
        return prompt_player()

    return p_choice


def compare(playerChoice, cpuChoice):
    results = {
        ('Paper', 'Rock'): True,
        ('Paper', 'Scissors'): False,
        ('Rock', 'Paper'): False,
        ('Rock', 'Scissors'): True,
        ('Scissors', 'Paper'): True,
        ('Scissors', 'Rock'): False
    }

    return results[(playerChoice, cpuChoice)]


def play():
    p_choice = prompt_player()
    cpu_choice = choice(game_choices)

    if p_choice == cpu_choice:
        return print('Tie!\n')
    elif compare(p_choice, cpu_choice):
        return print('You Win!\n')
    else:
        return print('You Lose!\n')


def play_again():
    begin = input(
        "Would you like to play again? ").lower().capitalize()

    if begin == "No" or begin == "N":
        print("Game Over")
        return False
    elif begin == "Yes" or begin == "Y":
        print("Okie, give me a second!\n")
        return True
    else:
        print("You have to type Yes or No")
        return play_again()


def game_start():
    print("Welcome to Rock, Paper, Scissors!")

    keep_playing = True
    while keep_playing:
        play()
        keep_playing = play_again()


game_start()
