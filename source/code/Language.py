import re
class Language:
    def __init__(self):
        self.patternLanguage = "[^sxocqnmwpfyheljrdgui]"
    def isInLanguage(self, word):
        position = 0
        if len(word) <= 0 :
            raise Exception("Word empty!!")
        
        patronAlphabet = re.compile(self.patternLanguage)
        matchOutLanguage = patronAlphabet.search(word)
        if matchOutLanguage == None:
            return True
        
        if matchOutLanguage.span()[1] > position:
            raise Exception("Word no valid !!")
        return True
