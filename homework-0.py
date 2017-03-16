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
    print("letter = ", letter)
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
    print("part 1", slice)
    print(slice)
    print("part 2 -- consonants only")
    print(split_by_vowels(slice, False))
    print("part 3 -- vowels only")
    print(split_by_vowels(slice, True))

#now do it!
main_list()

### try using a dict instead of a list.
def main_dict():
    print ("########")
    print ("try again using a dict")
    letters_dict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9}
    number = 0
    number = int(input("Please enter an integer from 1 to 10 >> "))

    # get the slice, by looking across dict and comparing value to input number
    slice_dict = {}
    for k, v in letters_dict.items():
        if v < number:
          slice_dict[k] = v

    print("part 1 as dict")
    print(slice_dict)


    # take the slice and look across, splitting into vowels and consonants
    # can use the same is_vowel function as the list example
    vowel_dict = {}
    cons_dict = {}
    for k, v in slice_dict.items():
        if is_vowel(k):
            vowel_dict[k] = v
        else:
            cons_dict[k] = v

    print("part 2 -- consonants only as dict")
    print(cons_dict)
    print("part 3 -- vowels only as dict")
    print(vowel_dict)



main_dict()
