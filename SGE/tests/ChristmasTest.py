#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import unittest
from src.Christmas import FunWithSnow

clase = FunWithSnow()

class MyTest(unittest.TestCase):
    
    def testIsPalindrome(self):
        self.assertTrue(clase.isPalindrome("A Mercedes �se de crema"))
        self.assertTrue(clase.isPalindrome("Ana, la taca�a catalana"))
        self.assertFalse(clase.isPalindrome("dado"))
        self.assertFalse(clase.isPalindrome("ddia"))
    
    def testReverseWordsOnAString(self):
        self.assertEqual(clase.reverse(['esta', 'casa', 'es', 'un', 'ruina']), "atse asac se nu aniur")
        
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()