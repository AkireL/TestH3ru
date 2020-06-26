import re
from Language import Language

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Preposition:
    def __init__(self, language:Language):
        self.language = language
        
    """
        The prepositions are the words of exactly 6 letters 
        which end in a foo letter and do not contain the letter u
    """
    def isPreposition(self, word):
        if(self.language.isInLanguage(word) == False):
            return False
        
        if(not len(word) == 6):
            return False
        
        patronAlphabet = re.compile("u")
        matchContainsU = patronAlphabet.search(word)
        
        if matchContainsU != None:
            return False
        
        patronAlphabet = re.compile("[sxmpfd]$")
        matchEndsFooLetter = patronAlphabet.search(word)
        
        if matchEndsFooLetter == None:
            return False
        
        return (matchEndsFooLetter.span()[1]) > 0
