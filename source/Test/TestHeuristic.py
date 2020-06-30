import unittest
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from source.code.Heuristic import Heuristic

from source.code import Constant
"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestHeuristic(unittest.TestCase):  
        
    def setUp(self):
        self.h = Heuristic()   
        
        # TEST VERB
    def test_classify_verb(self):
        self.assertEqual(self.h.classify("xoxoxo"), {'word': 'xoxoxo', 'type': Constant.HERUGLON_VERB })        
       

        
        # TEST VERB SUBJUNCTIVE
    def test_classify_subjunctive(self):
        self.assertEqual(self.h.classify("oxooxo"), {'word': 'oxooxo', 'type':Constant.HERUGLON_VERB_SUBJUNCTIVE})        
        self.assertEqual(self.h.classify("oxoxoxo"), {'word': 'oxoxoxo', 'type':Constant.HERUGLON_VERB_SUBJUNCTIVE})   

        # TEST PREPOSITION        
    def test_classify_preposition(self):
        self.assertEqual(self.h.classify("pwdood"), {'word': 'pwdood', 'type':Constant.HERUGLON_PREPOSITION})
        self.assertEqual(self.h.classify("xoxoxs"), {'word': 'xoxoxs', 'type': Constant.HERUGLON_PREPOSITION})        
        

        # TEST NUMBERS        
    def test_classify_number(self):
        self.assertEqual(self.h.classify("puxood"), {'word': 'puxood', 'type': Constant.HERUGLON_NUMBER, 'number': 51536768} )
        self.assertEqual(self.h.classify("puxod"),  {'word': 'puxod', 'type': Constant.HERUGLON_NUMBER, 'number': 2576768})
        self.assertEqual(self.h.classify("xoxo"), {'word': 'xoxo', 'type': Constant.HERUGLON_NUMBER, 'number': 16441})        
        self.assertEqual(self.h.classify("gxjrc"), {'word': 'gxjrc', 'type': Constant.HERUGLON_NUMBER_PRETTY, 'number': 605637})
        self.assertEqual(self.h.classify("shoce"),  {'word': 'shoce', 'type': Constant.HERUGLON_NUMBER_PRETTY, 'number': 1945020})
        self.assertEqual(self.h.classify("xxoxoxs"), {'word': 'xxoxoxs', 'type': Constant.HERUGLON_NUMBER, 'number': 3528821})  
        self.assertEqual(self.h.classify("xxoxoxs"), {'word': 'xxoxoxs', 'type': Constant.HERUGLON_NUMBER, 'number': 3528821})  

                       
if __name__ == '__main__':
    unittest.main()