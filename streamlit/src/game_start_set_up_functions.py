import random

def get_letters_to_start():
    '''
    Returns 3 to 5 letters to play the game
    '''

    # Reads all English words
    with open('../data/words_alpha.txt') as f:
        raw = f.readlines()


    # Cleans tabs
    words = []
    for i in raw:

        words.append(i.rstrip('\n'))


    # Picks a random word
    def get_random_word(words):

        random_pick_of_the_game = random.choice(words)

        return random_pick_of_the_game
    

    # Picks a random number of letters, from 3 to 5
    random_pick_of_the_game = ''

    while not len(random_pick_of_the_game) >= 3:

        random_pick_of_the_game = get_random_word(words)

    three_to_five_letters = random.randint(3, 5)


    # Gets starting letter position
    def get_starting_letter_position(length):

        starting_position = random.randint(0, length)

        return starting_position
    

    # Picks a random starting letter position
    starting_position = len(random_pick_of_the_game)

    while not (starting_position + three_to_five_letters - 1) < len(random_pick_of_the_game):

        starting_position = get_starting_letter_position(len(random_pick_of_the_game))
    

    # Creates a list with the letters to start the game
    chosen_letters_to_start = []

    for i in range(0, three_to_five_letters):

        chosen_letters_to_start.append(random_pick_of_the_game[starting_position + i])


    # Joins letters
    letters_joined = ''

    for c in chosen_letters_to_start:

        letters_joined += c

    return letters_joined.upper()
