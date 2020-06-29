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

    def setUp(self):
        self.h = Language()         
        self.n = Numbers(Verb(Language() ),Preposition(Language()) )    
        self.v = Verb(Language() )     
        self.p = Preposition(Language())     
        
        
    def test_noExistInLanguage(self):
        with self.assertRaises(Exception) as e:
            self.h.isInLanguage("a")
        self.assertEqual("Word no valid !!", str(e.exception))
        
        
    def test_wordEmptyException(self):
        with self.assertRaises(Exception) as e:
            self.h.isInLanguage("")
        self.assertEqual("Word empty!!", str(e.exception))
        
        
    def test_isInLanguage(self):  
        self.assertEqual(self.h.isInLanguage("xoxox"), True)
        
    def test_isVerbException(self):
        with self.assertRaises(Exception) as e:
            self.v.isVerb("")
        self.assertEqual("Word empty!!", str(e.exception))
        
        
    def test_isVerb(self):
        self.assertEqual(self.v.isVerb("xoxo"), False)        
        self.assertEqual(self.v.isVerb("xoxox"), False)        
        self.assertEqual(self.v.isVerb("xoxoxo"), True)        
        self.assertEqual(self.v.isVerb("xoxoxs"), False)        

    def test_isVerbSubjunctiveException(self):
        with self.assertRaises(Exception) as e:
            self.v.isVerbSubjunctive("")
        self.assertEqual("Word empty!!", str(e.exception))
        
    def test_isVerbSubjunctive(self):  
        
        self.assertEqual(self.v.isVerbSubjunctive("xoxo"), False)        
        self.assertEqual(self.v.isVerbSubjunctive("xoxox"), False)        
        self.assertEqual(self.v.isVerbSubjunctive("oxooxo"), True)        
        self.assertEqual(self.v.isVerbSubjunctive("xxoxoxs"), False)  
        self.assertEqual(self.v.isVerbSubjunctive("oxoxoxo"), True)   

    def test_isPrepositionException(self):
        with self.assertRaises(Exception) as e:
           self.p.isPreposition("")
        self.assertEqual("Word empty!!", str(e.exception))

        
    def test_isPreposition(self):  
        self.assertEqual(self.p.isPreposition("puxod"), False)
        self.assertEqual(self.p.isPreposition("puxood"), False)
        self.assertEqual(self.p.isPreposition("pwdood"), True)

    def test_isNumberException(self):
        with self.assertRaises(Exception) as e:
           self.n.isNumber("")
        self.assertEqual("Word empty!!", str(e.exception))
        
    def test_isNumber(self):  
        self.assertEqual(self.n.isNumber("gxjrc"), True)
        self.assertEqual(self.n.isNumber("pwdood"), False)
                       
if __name__ == '__main__':
    unittest.main()