import unittest
from Heuristic import Heuristic
import Constant

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestHeuristic(unittest.TestCase):  
        
        # TEST VERB
    def test_classify_verb(self):
        h = Heuristic()       
        self.assertEqual(h.classify("xoxoxo"), {'word': 'xoxoxo', 'type': Constant.HERUGLON_VERB })        

        
        # TEST VERB SUBJUNCTIVE
    def test_classify_subjunctive(self):
        h = Heuristic()
        # self.assertEqual(h.classify("xoxox"), False)        
        self.assertEqual(h.classify("oxooxo"), {'word': 'oxooxo', 'type':Constant.HERUGLON_VERB_SUBJUNCTIVE})        
        self.assertEqual(h.classify("oxoxoxo"), {'word': 'oxoxoxo', 'type':Constant.HERUGLON_VERB_SUBJUNCTIVE})   

        # TEST PREPOSITION        
    def test_classify_preposition(self):
        h = Heuristic()
        self.assertEqual(h.classify("pwdood"), {'word': 'pwdood', 'type':Constant.HERUGLON_PREPOSITION})
        self.assertEqual(h.classify("xoxoxs"), {'word': 'xoxoxs', 'type': Constant.HERUGLON_PREPOSITION})        
        

        # TEST NUMBERS        
    def test_classify_number(self):
        h = Heuristic()
        self.assertEqual(h.classify("puxood"), {'word': 'puxood', 'type': Constant.HERUGLON_NUMBER, 'number': 51536768} )
        self.assertEqual(h.classify("puxod"),  {'word': 'puxod', 'type': Constant.HERUGLON_NUMBER, 'number': 2576768})
        self.assertEqual(h.classify("xoxo"), {'word': 'xoxo', 'type': Constant.HERUGLON_NUMBER, 'number': 16441})        
        self.assertEqual(h.classify("gxjrc"), {'word': 'gxjrc', 'type': Constant.HERUGLON_NUMBER_PRETTY, 'number': 605637})
        self.assertEqual(h.classify("shoce"),  {'word': 'shoce', 'type': Constant.HERUGLON_NUMBER_PRETTY, 'number': 1945020})
        self.assertEqual(h.classify("xxoxoxs"), {'word': 'xxoxoxs', 'type': Constant.HERUGLON_NUMBER, 'number': 3528821})  

                       
if __name__ == '__main__':
    unittest.main()