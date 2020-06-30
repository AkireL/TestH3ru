import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from source.code.Heuristic import Heuristic
from source.code.Text import Text
from source.code.Order import Order
from source.code import Constant

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class CtrlHeuristic:
    def __init__(self):
        self.h = Heuristic()
        self.t = Text()
        self.o = Order()
        
    def execute(self, textL):
        arrayResult = {
            Constant.HERUGLON_NAMES[ Constant.HERUGLON_PREPOSITION]: 0,
            Constant.HERUGLON_NAMES[ Constant.HERUGLON_VERB]: 0,
            Constant.HERUGLON_NAMES[ Constant.HERUGLON_VERB_SUBJUNCTIVE]: 0,
            Constant.HERUGLON_NAMES[ Constant.HERUGLON_NUMBER_PRETTY]:0,
            "Vocabulary": None
        }
        
        listPrettyNumber = {}
        arrayPharagrap = self.t.getWords(textL)
        vocabulary = {}
        
        for word in arrayPharagrap:
            class_word = self.h.classify(word)
            class_word_type = class_word['type'] 
            
            if(class_word_type == Constant.HERUGLON_UNKNOWN):
                pass
            
            vocabulary[word] = word
            
            if(class_word_type == Constant.HERUGLON_NUMBER):
                pass
            
            if(class_word_type == Constant.HERUGLON_NUMBER_PRETTY):
                listPrettyNumber[word] = word
            elif(class_word_type == Constant.HERUGLON_VERB):
                arrayResult[Constant.HERUGLON_NAMES[ Constant.HERUGLON_VERB]] += 1
            elif(class_word_type == Constant.HERUGLON_VERB_SUBJUNCTIVE):
                arrayResult[Constant.HERUGLON_NAMES[ Constant.HERUGLON_VERB]] += 1
                arrayResult[Constant.HERUGLON_NAMES[ Constant.HERUGLON_VERB_SUBJUNCTIVE]] += 1
            elif(class_word_type == Constant.HERUGLON_PREPOSITION):
                arrayResult[Constant.HERUGLON_NAMES[ Constant.HERUGLON_PREPOSITION]] += 1
        
        arrayResult[Constant.HERUGLON_NAMES[ Constant.HERUGLON_NUMBER_PRETTY]] = len(listPrettyNumber)
        
        listWords = self.o.prepare(vocabulary.keys())
        listOrderVocabulary = self.o.do(listWords)
        arrayResult['Vocabulary'] = listOrderVocabulary
        
        return arrayResult

