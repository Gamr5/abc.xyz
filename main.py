# Made by Gamr5

lettersUpper = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLetter(num, case=1):
    if case == 1:
        return letters[num]
    elif case == 0:
        return lettersUpper[num]

def findPos(letter):
    return letters.index(letter.lower())

def shift(chars, shiftnum):
    shifted = []
    for char in chars:
        if char.isalpha():
            shifted_letter = findLetter((findPos(char) + shiftnum) % 26, case=char.islower())
            shifted.append(shifted_letter)
        else:
            shifted.append(char)
    return ''.join(shifted)


