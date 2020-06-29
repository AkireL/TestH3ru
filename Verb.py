import re
from Language import Language

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Verb:
    def __init__(self, language:Language):
        self.language = language
        self.minLenghtVerb = 6
        self.patternEndWord = "[ocqnwyheljrgi]$"
        self.patternStartToEndWord = "^[ocqnwyheljrgi][sxocqnmwpfyheljrdgui]*[ocqnwyheljrgi]$"
    """
        verbs are words of 6 letters or more that end in a bar letter
    """
    def isVerbSubjunctive(self, word):
        if(self.language.isInLanguage(word) == False):
            return False
        
        if(len(word) < self.minLenghtVerb):
            return False
        
        patronAlphabet = re.compile(self.patternStartToEndWord)
        value = patronAlphabet.search(word)
        if value == None:
            return False
        return (patronAlphabet.search(word).span()[1]) > 0
    """
        verbs are words of 6 letters or more that end in a bar letter
    """
    def isVerb(self, word):
        if(self.language.isInLanguage(word) == False):
            return False
        
        if(len(word) < self.minLenghtVerb):
            return False
        
        patronAlphabet = re.compile(self.patternEndWord)
        matchEndsBarLetter = patronAlphabet.search(word)
        if matchEndsBarLetter == None:
            return False
        return (matchEndsBarLetter.span()[1]) > 0
        