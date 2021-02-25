import unittest
import sum

class testSum(unittest.TestCase):
    def test_sum(self):
        result = sum.sum()
        self.assertEqual(result,55)
        
if __name__ == "__main__":
    unittest.main()
    
