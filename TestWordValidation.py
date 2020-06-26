import unittest
from Language import Language
from Verb import Verb
from Preposition import Preposition
from Numbers import Numbers

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestWordValidation(unittest.TestCase):

    def test_isInLanguage(self):  
        self.h = Language()     
        self.assertEqual(self.h.isInLanguage("xoxox"), True)

    def test_isVerb(self):
        self.h = Verb( Language() )     
        self.assertEqual(self.h.isVerb("xoxo"), False)        
        self.assertEqual(self.h.isVerb("xoxox"), False)        
        self.assertEqual(self.h.isVerb("xoxoxo"), True)        
        self.assertEqual(self.h.isVerb("xoxoxs"), False)        
 
    def test_isVerbSubjunctive(self):  
        self.h = Verb(Language() )     
        
        self.assertEqual(self.h.isVerbSubjunctive("xoxo"), False)        
        self.assertEqual(self.h.isVerbSubjunctive("xoxox"), False)        
        self.assertEqual(self.h.isVerbSubjunctive("oxooxo"), True)        
        self.assertEqual(self.h.isVerbSubjunctive("xxoxoxs"), False)  
        self.assertEqual(self.h.isVerbSubjunctive("oxoxoxo"), True)   

    def test_isPreposition(self):  
        self.h = Preposition(Language())     
        self.assertEqual(self.h.isPreposition("puxod"), False)
        self.assertEqual(self.h.isPreposition("puxood"), False)
        self.assertEqual(self.h.isPreposition("pwdood"), True)

    def test_isNumber(self):  
        self.h = Numbers(Verb(Language() ),Preposition(Language()) )     
        self.assertEqual(self.h.isNumber("gxjrc"), True)
        self.assertEqual(self.h.isNumber("pwdood"), False)
                       
if __name__ == '__main__':
    unittest.main()