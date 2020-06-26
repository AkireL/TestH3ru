import unittest
from Numbers import Numbers
from Language import Language
from Verb import Verb
from Preposition import Preposition

"""
    
    
    @author Erika Leonor Basurto Munguia <iamdleonor@gmail.com>
    @version 1.0.0
"""
class TestNumber(unittest.TestCase):
    def test_getValue(self):
        n = Numbers(Verb(Language()), Preposition(Language()))
        self.assertEqual(n.getValue("gxjrc"), 605637)
        
         
if __name__ == '__main__':
    unittest.main()