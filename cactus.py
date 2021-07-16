from dialogue import intro_dialogue, print_choices, get_initial_choices


class Player():

    def init__(self, name: str):
        self.name = name
        self.attack = 5
        self.inventory = []






def start_game():

    name = input('What is your name? \n\n> ')
    intro_dialogue(name)

    print_choices(get_initial_choices())




if __name__ == '__main__':
    start_game()



