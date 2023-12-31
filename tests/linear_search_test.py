import unittest
from searching_algorithm.linear_search import LinearSearch

class LinearSearchTest(unittest.TestCase):
    def setUp(self):
        # Initialize a LinearSearchTest object
        self.search_algorithm = LinearSearch()
    
    def test_linear_search_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        result = self.search_algorithm.search(arr,target)
        self.assertEqual(result,"The target value 3 found at index no: 2")
    
    def test_linear_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 6
        result = self.search_algorithm.search(arr,target)
        self.assertEqual(result, "The target value 6 not found, index: -1")

if __name__ == "__main__":
    unittest.main()