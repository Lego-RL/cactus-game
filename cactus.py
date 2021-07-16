from pickle import FALSE
from dialogue import intro_dialogue, print_options, get_initial_options
from input import get_input


class Player():

    def init__(self, name: str):
        self.name = name
        self.attack = 5
        self.inventory = []






def start_game():
    #back represents if user can come back to set of choices after
    #their chosen option plays out
    back = False

    name = input('What is your name? \n\n> ')
    intro_dialogue(name)

    options = get_initial_options()

    # while not back:
    while True:
        print_options(options)

        choice = get_input() - 1 #subtract 1 from choice because key indexes start at 0
        back = options[choice]['back']

        if options[choice]['next'] == 'placeholder':
            print('Path not implemented yet!')

        else:
            options[choice]['next']() #run next function for story to progress

        del options[choice]
        #somehow switch between options for next path or stick with current options
        #if necessary


    




if __name__ == '__main__':
    start_game()



