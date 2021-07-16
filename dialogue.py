from input import get_input

def print_options(options: dict):
    options_str = ''

    end = len(options) - 1 if "description" in options.keys() else len(options)

    for i in range(end):

        options_str += f"{i+1}: {options[i]['text']}\n"

    if "description" in options.keys():
        print(options["description"])
    
    print(options_str)

    print('> ', end='') #prepare input to be taken



def intro_dialogue(name: str) -> None:
    
    intro = f'''
    You are a cactus. A cactus named {name}.
    You don't know where you are.
    You don't know how you got here.
    You just know you are full of thorns, and a will to live.
    Good luck.
    '''

    print(intro)


def initial_inventory_check():
    '''
    This function will only be ran once, in the case that the player checks
    their inventory during the first path. Therefore, inventory should always
    be empty at this point.
    '''

    mocking_text = '''
    You have nothing. You just woke up as a cactus in a cave, what did you expect
    to have with you? 
    '''

    print(mocking_text)




#TODO: fill in "next" fields for each path

def get_initial_options() -> list:

    '''
    Return dictionary of possible options & the function that should be ran next in order
    to advance the story. Also has a "back" field to denote if you will come back to these
    options after selecting this option. For example, back is True for options[4] so once
    you check your inventory you will return to this set of options (with options[4] removed).
    '''

    options = dict()

    options["description"] = '''
    You are just inside the entrance of a dark, uninviting cave. You realize you have absolutely
    no supplies to work with for the time being. Unfamiliar with your surroundings, you decide your
    first course of action will be...
'''
    

    options[0] = {
        "text": "Leave the cave. You're a cactus, why are you in the cave anyway?",
        "next": "placeholder",
        "back": False
    }

    options[1] = {
        "text": "Attempt to interpret the odd drawings on the walls.",
        "next": "placeholder",
        "back": False
    }

    options[2] = {
        "text": "Cry out for help.",
        "next": "placeholder",
        "back": False
    }

    options[3] = {
        "text": "Do nothing. You're a cactus, this is literally what you were made for.",
        "next": "placeholder",
        "back": False
    }

    options[4] = {
        "text": "Check your inventory.",
        "next": initial_inventory_check,
        "back": True
    }


    return options 


