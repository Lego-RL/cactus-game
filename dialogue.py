

def print_choices(choices: dict):
    choices_str = ''

    end = len(choices) - 1 if "description" in choices.keys() else len(choices)

    for i in range(end):

        choices_str += f"{i+1}: {choices[i]['text']}\n"

    if "description" in choices.keys():
        print(choices["description"])
    
    print(choices_str)



def intro_dialogue(name: str) -> None:
    
    intro = f'''
    You are a cactus. A cactus named {name}.
    You don't know where you are.
    You don't know how you got here.
    You just know you are full of thorns, and a will to live.
    Good luck.
    '''

    print(intro)



def get_initial_choices() -> list:

    '''
    Return dictionary of possible choices & the function that should be ran next in order
    to advance the story. 
    '''

    choices = dict()

    choices["description"] = '''
    You are just inside the entrance of a dark, uninviting cave. You realize you have absolutely
    no supplies to work with for the time being. Unfamiliar with your surroundings, you decide your
    first course of action will be...
'''
    

    choices[0] = {
        "text": "Leave the cave. You're a cactus, why are you in the cave anyway?",
        "next": "placeholder"
    }

    choices[1] = {
        "text": "Attempt to interpret the odd drawings on the walls.",
        "next": "placeholder"
    }

    choices[2] = {
        "text": "Cry out for help.",
        "next": "placeholder"
    }

    choices[3] = {
        "text": "Do nothing. You're a cactus, this is literally what you were made for.",
        "next": "placeholder"
    }


    return choices 


