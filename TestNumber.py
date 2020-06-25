import unittest
from Numbers import Numbers

class TestNumber(unittest.TestCase):
    def test_getValue(self):
        n = Numbers()
        self.assertEqual(n.getValue("gxjrc"), 605637)
        
         
if __name__ == '__main__':
    unittest.main()