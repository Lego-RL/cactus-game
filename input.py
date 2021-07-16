


def get_input() -> int:

    choice = None

    while not choice:
        choice = input()

        try:
            choice = int(choice)

        except ValueError:
            print('\nInvalid choice, try again.\n> ', end='')
            choice = None
            continue

    
    
    return choice
