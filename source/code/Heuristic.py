import re
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from source.code.Language import Language
from source.code.Verb import Verb
from source.code.Preposition import Preposition
from source.code.Numbers import Numbers
# import source.code.Constant
from source.code import Constant


"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class Heuristic:
    def __init__(self):
        self.lObj = Language()
        self.vObj = Verb(self.lObj)
        self.pObj = Preposition(self.lObj)
        self.nObj = Numbers(self.vObj, self.pObj)
        
    def classify(self, word):
        try:
            self.lObj.isInLanguage(word)
            
            if self.nObj.isNumber(word):
                value = self.nObj.getValue(word)
                return {'word':word, 'type': Constant.HERUGLON_NUMBER_PRETTY, 'number': value } if self.nObj.isPretty(value) else {'word':word, 'type': Constant.HERUGLON_NUMBER, 'number': value}
            if self.vObj.isVerbSubjunctive(word):
                return {'word':word, 'type':Constant.HERUGLON_VERB_SUBJUNCTIVE}
            if self.vObj.isVerb(word):
                return {'word':word, 'type':Constant.HERUGLON_VERB}
            if self.pObj.isPreposition(word):
                return {'word':word, 'type':Constant.HERUGLON_PREPOSITION}
            
            return {'word':word, 'type':Constant.HERUGLON_UNKNOWN, 'error': "Unknown word" }
        except:
            return {'word':word, 'type':Constant.HERUGLON_UNKNOWN, 'error': sys.exc_info()[1] }
      