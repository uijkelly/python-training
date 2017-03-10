#python3
#
# Jessica A Kelly
#
# using homework0.pdf as guide


def is_vowel(letter):
    """
    :param letter: letter to check
    :return: true if a vowel, false otherwise
    """
    if letter in ["A","E","I","O","U"]:
        return True
    else:
        return False

def split_by_vowels(list_letters,keep_vowels):
    """
    :return: list of strings that are vowels or all non-vowels
    :param list_letters: a list of letters to slice up
    :param keep_vowels: is boolean indicator of vowels (True) or not (False)
    """
    ret_list = []
    for i in range(0,len(list_letters)):
        #print('i is now:', i)
        if is_vowel(list_letters[i]) == keep_vowels:
            ret_list.append(list_letters[i])

    return ret_list

def main_list():
    print("homework 0")
    letters = ["A","B","C","D","E","F","G","H","I","J"]
    number = 0
    number = int(input("Please enter an integer from 1 to 10 >> "))
    slice = letters[0:number] #start at 0 and go for length of number
    print("part 1")
    print(slice)
    print("part 2 -- consonants only")
    print(split_by_vowels(slice, False))
    print("part 3 -- vowels only")
    print(split_by_vowels(slice, True))

#now do it!
main_list()
