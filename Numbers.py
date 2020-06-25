import re
from Verb import Verb
from Preposition import Preposition
class Numbers:
    def __init__(self, verb:Verb, preposition: Preposition):
        self.verb = verb
        self.preposition = preposition
    
    alphabetDictionary = {
        's': 0,
        'x': 1,
        'o': 2,
        'c': 3,
        'q': 4,
        'n': 5,
        'm': 6,
        'w': 7,
        'p': 8,
        'f': 9,
        'y': 10,
        'h': 11,
        'e': 12,
        'l': 13,
        'j': 14,
        'r': 15,
        'd': 16,
        'g': 17,
        'u': 18,
        'i': 19 
    }
    
    def isNumber(self, word):
        return False if self.verb.isVerb(word) or self.preposition.isPreposition(word) else True
    
    """
        Convert to Numbers
    """
    def getValue(self, word):
        base = 20
        sum = 0
        for item in range(len(word)):
            v = (self.alphabetDictionary[ word[item]] )
            positionValue = v * base ** item
            sum += positionValue
            # print(f"{item}:" + word[item] + " = " + f"{v} * 20 ^ {item} = "+ f"{positionValue}")
        return sum
    
    """
        Number pretty
        - it is greater than or equal to 81827
        - it is divisible by 3
    """
    def isPretty(self, value: int):
        minValue = 81827
        divided = 3
        return value > minValue and value % divided == 0

# v = Numbers()
# number = v.getValue("gxjrc")  
# pretty = v.isPretty(number)
# print(f"{number} is pretty: {pretty}")   
        