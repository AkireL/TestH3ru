import unittest
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from source.code.Numbers import Numbers
from source.code.Language import Language
from source.code.Verb import Verb
from source.code.Preposition import Preposition

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