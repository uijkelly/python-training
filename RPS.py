# Classwork-1
#
# using class shell, but with lots of trying things
#
# the following is how you import a module you want to use that isn't automatically included
# We're going to use the "randint" function from the "random" module
# So that we can simulate the computer playing Rock Paper Scissors
#
# Jessica A Kelly
#
# I'd really like to use tuples and a more complicated dict, ideally (because that's
# the new to me python piece), but we aren't there in this particular
# class, so will try after simple if-elses etc.

import random

def convert_choice_to_char(int_choice):
    """
    converts integer version of choice to a character
    """
    rps_dict = {"R": 0, "P":1, "S": 2}
    for k, v in rps_dict.items():
        if v == int_choice:
            #print("found choice!")
            return k

def convert_choice_to_desc(char_choice):
    """
    converts character choice to long description
    """
    rps_dict = {"R": "Rock", "P":"Paper", "S":"Scissors"}
    return rps_dict[char_choice]

def compare_choice(user_choice, computer_choice):
    """
    compares user and computer choice and returns string of who won
    # Rock beats Scissors (R > S)
    # Paper beats Rock (P > R)
    # Scissors beats Paper (S > P)
    Note: I really dislike this here function
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "R":
        if computer_choice == "S":
            return "User Wins! Rock beats Scissors!"
        else: # must be Paper
            return "User Loses! Computer wins. Paper covers Rock!"
    elif user_choice == "P":
        if computer_choice == "R":
            return "User Wins! Paper covers Rock!"
        else: # must be Scissors
            return "User Loses! Computer wins. Scissors cut Paper."
    else: # user_choice must be Scissors
        if computer_choice == "R":
            return "User Loses! Computer wins. Rock beats Scissors."
        else: # must be Paper
            return "User Wins! Scissors cut Paper!"

def compare_with_ifs(user_choice, computer_choice):
    """
    Decide who wins with if-elses
    """
    print ("")
    print ("##### Who wins by a set of if-else statements ######")
    #Brute force. Nothing overly clever
    # And lets print out what we have chosen and what the computer chose
    print ("User Choice is: ", convert_choice_to_desc(user_choice))
    #print ("Computer Choice is: ", computer_choice)
    print("Computer Choice is: ", convert_choice_to_desc(computer_choice))

    # Now to decide who wins
    print(compare_choice(user_choice, computer_choice))

def compare_with_tuple(user_choice, computer_choice):
    """
    Decide who wins with a tuple and a dict
    It's so much shorter than the if-elses and easier
    to debug
    """
    print("")
    print ("##### Trying again with different code ######")
    print ("User Choice is: ", convert_choice_to_desc(user_choice))
    print("Computer Choice is: ", convert_choice_to_desc(computer_choice))

    # create a dict that will tell us who wins and then just look for the tuple.
    # key is the game result, and the value is the tuples that give that result.
    all_games = { "User Wins!!": (("P","R"), ("R","S"), ("S","P")), # this is a game_set below
                  "It's a Tie.": (("P","P"), ("R","R"), ("S","S")), # this is a game_set below
                  "Computer Wins, sorry.": (("R","P"), ("S","R"), ("P","S")) # this is a game_set below
    }
    # create tuple of user and computer choices
    this_game = (user_choice, computer_choice)

    # now look across the dict and print the result
    for a_game_set in all_games:
        if this_game in all_games[a_game_set]: # search the row for this game
            # print the result!
            print(a_game_set) # the game_set is the key, the tuples are the values


def main():
    ### Get user input. Same in both examples I want to try.
    keep_playing = True #TODO
    results = (0,0,0) # wins, loses and ties
    while keep_playing:
        valid_choice = False
        choices = ["R","P","S"]
        while not valid_choice:
            try:
                user_choice = input("Would you like to play Rock (R), Paper (P), or Scissors (S)? ")
                if user_choice in choices:
                    valid_choice = True
                else:
                    print("Case Matters! Try again!")
            except:
                print("Unknown Error at user input")

        # generate the computer_choice
        # one way
        # computer_choice = random.randint(0, 2)
        # computer_choice_char = convert_choice_to_char(computer_choice)
        # like this way better, randomly generate index and then use the choices
        # list in order to get the element.
        computer_choice = choices[random.randint(0,2)]

        # this is more true to the class at this point, but no
        # need to run both all the time!
        # compare_with_ifs(user_choice, computer_choice)

        compare_with_tuple(user_choice, computer_choice)

        keep_playing = False




# Call the main function
main()
