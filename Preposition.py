import re
from Language import Language

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Preposition:
    def __init__(self, language:Language):
        self.language = language
        self.patternOutherU = "u"
        self.patternFooLetters = "[sxmpfd]$"
        self.minLenghtPreposition = 6
        
    """
        The prepositions are the words of exactly 6 letters 
        which end in a foo letter and do not contain the letter u
    """
    def isPreposition(self, word):
        if(self.language.isInLanguage(word) == False):
            return False
        
        if(not len(word) == self.minLenghtPreposition):
            return False
        
        patronAlphabet = re.compile(self.patternOutherU)
        matchContainsU = patronAlphabet.search(word)
        
        if matchContainsU != None:
            return False
        
        patronAlphabet = re.compile(self.patternFooLetters)
        matchEndsFooLetter = patronAlphabet.search(word)
        
        if matchEndsFooLetter == None:
            return False
        
        return (matchEndsFooLetter.span()[1]) > 0
