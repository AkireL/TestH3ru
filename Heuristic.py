import re
from Language import Language
from Verb import Verb
from Preposition import Preposition
from Numbers import Numbers

class Heuristic:
    def lew(self, word):
        l = Language()
        v = Verb(l)
        p = Preposition(l)
        n = Numbers(v,p)
        
        # return(l.isInLanguage(word))
        # return v.isVerb(word)
        # return v.isVerbSubjunctive(word)
        # return p.isPreposition(word)
        return n.isNumber(word)
        
    

    
    
    
    


try:
    h = Heuristic()
    word = "qoxopq"
    r = h.lew(word)
    print(f"{word} is {r}")
except Exception as error:
    print(error)