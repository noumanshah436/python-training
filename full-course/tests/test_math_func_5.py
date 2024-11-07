import unittest
from math_func import Math

class TestMath(unittest.TestCase):
    
    def test_add(self):
        math = Math()
        
        # Test adding two positive numbers
        result = math.add(2, 3)
        self.assertEqual(result, 5)
        
        # Test adding a positive and a negative number
        result = math.add(5, -2)
        self.assertEqual(result, 3)
        
        # Test adding two negative numbers
        result = math.add(-1, -1)
        self.assertEqual(result, -2)

# if __name__ == '__main__':
#     unittest.main()


# ***************************************

# run with pytest
# pytest test_math_classes_5.py -v