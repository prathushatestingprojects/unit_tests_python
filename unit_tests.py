
# Importing relevant packages for testing
# unittest is the most popular one for unit tests
import unittest
# Importing the module various_methods
from various_methods import VariousMethods

# Creating object so that we can test its built in methods 
obj = VariousMethods()

# Testing class

class TestVariousMethods(unittest.TestCase):
    
    # Testing first method 
    def test_ConvertToAtlasCopcoString(self):
        # testing case if 1 would return 1 or not
        self.assertEqual(obj.ConvertToAtlasCopcoString(1),'1')
        # testing if a number divisible by both 5 and 3 would return AtlasCopco or not
        self.assertEqual(obj.ConvertToAtlasCopcoString(15),'AtlasCopco')
        # testing if a number only divisible by 3 would return Atlas or not
        self.assertEqual(obj.ConvertToAtlasCopcoString(9),'Atlas')
        # testing if a number only divisible by 3 would return Atlas or not
        self.assertEqual(obj.ConvertToAtlasCopcoString(87),'Atlas')
        # testing if a number only divisible by 5 would return Copco or not
        self.assertEqual(obj.ConvertToAtlasCopcoString(20),'Copco')


    # Testing whether the method will raise valueerror or not if the input is > 100   
    def test_ConvertToAtlasCopcoString_ValueError1(self):
        with self.assertRaises(ValueError):
              obj.ConvertToAtlasCopcoString(105)
              
    # Testing whether the method will raise valueerror or not if the input is < 1   
    def test_ConvertToAtlasCopcoString_ValueError2(self):
        with self.assertRaises(ValueError):
              obj.ConvertToAtlasCopcoString(0)
            
        
    # Testing second method
    def test_FindMax(self):
        # testing if maximum number between 1,2,3 is 3 or not
        self.assertEqual(obj.FindMax([1,2,3]),3)
        # testing if maximum number between 1,5,-7 is 5 or not
        self.assertEqual(obj.FindMax([1,5,-7]),5)
        # testing if maximum number between 100,23,1 is 100 or not
        self.assertEqual(obj.FindMax((100,23,1)),100)


    # Testing whether the method will raise valueerror or not if the input is empty list   
    def test_FindMax_ValueError1(self):
        with self.assertRaises(ValueError):
              obj.FindMax([])
              
    # Testing whether the method will raise valueerror or not if the input is None   
    def test_FindMax_ValueError2(self):
        with self.assertRaises(ValueError):
              obj.FindMax(None)
        
    
# run this module directly by calling unittest in our main
if __name__== '__main__':
    unittest.main()