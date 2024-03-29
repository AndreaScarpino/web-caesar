import string
def alphabet_position(letter):
    """receive a letter and return its numeric position"""
    alph2pos = {}
    alph2pos = {
        "a" : 0, "A" : 0, "b" : 1, "B" : 1, "c": 2, "C": 2, "d": 3, "D": 3,
        "e": 4, "E": 4, "f": 5, "F": 5, "g": 6, "G": 6, "h": 7, "H": 7, "i": 8,
        "I": 8, "j": 9, "J": 9, "k": 10, "K": 10, "l": 11, "L": 11, "m": 12,
        "M": 12, "n": 13, "N": 13, "o": 14, "O": 14, "p": 15, "P": 15, "q": 16,
        "Q": 16, "r": 17, "R": 17, "s": 18, "S": 18, "t": 19, "T": 19, "u": 20,
        "U": 20, "v": 21, "V": 21, "w": 22, "W": 22, "x": 23, "X": 23, "y": 24,
        "Y": 24, "z": 25, "Z": 25
        }
    position = alph2pos[letter]
    return position

def rotate_character(char, rot):
    """receives a string(char) and an integer to rotate (rot), then returns
    a new string which has been rotated by rot number of spaces"""
    if char in string.digits or char in string.punctuation or char in string.whitespace:
        return char
    else:
        if char in string.ascii_lowercase:
            rotated = (alphabet_position(char) + rot) %26
            return string.ascii_lowercase[rotated]
        else:
            rotated = (alphabet_position(char) + rot) %26
            return string.ascii_uppercase[rotated]

def encrypt(text, rot):
    """receives a string(text) and an integer to rotate (rot) then returns
    the result of rotating the string to the right the rot number of spaces"""
    encrypted = ""
    for char in text:
        index = rotate_character(char, rot)
        encrypted = encrypted + index
    return encrypted
