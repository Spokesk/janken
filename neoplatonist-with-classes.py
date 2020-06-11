from random import choice

class Game:
    def _gen_choice(self):
        return choice(self.game_choices)

    def __init__(self):
        self.game_choices = ['Rock', 'Paper', 'Scissors']
        self.cpu_choice = self._gen_choice()

    def prompt_player(self):
        self.p_choice = input(
            "What do you choose Rock, Paper, or Scissors? ").lower().capitalize()

        if self.p_choice not in self.game_choices:
            print("You did not specify a choice. Choose Rock, Paper, or Scissors. ")
            self.prompt_player()

    def compare(self, playerChoice, cpuChoice):
        results = {
            ('Paper', 'Rock'): True,
            ('Paper', 'Scissors'): False,
            ('Rock', 'Paper'): False,
            ('Rock', 'Scissors'): True,
            ('Scissors', 'Paper'): True,
            ('Scissors', 'Rock'): False
        }

        return results[(playerChoice, cpuChoice)]

    def play(self):
        self.prompt_player()

        self.cpu_choice = self._gen_choice()

        if self.p_choice == self.cpu_choice:
            return print('Tie!\n')
        if self.compare(self.p_choice, self.cpu_choice):
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
    game = Game()

    keep_playing = True
    while keep_playing:
        game.play()
        keep_playing = play_again()


game_start()
