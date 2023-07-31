# Made by Gamr5

lettersUpper = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o''p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def findLetter(num=int(), case=1):
    if (int(case) == 1):
        return letters[int(num)]
    elif (int(case) == 0):
        return lettersUpper[int(num)]

def findPos(letter) :
    return letters.index(letter.lower())