from typing import List
from search_pkg.search_base import SearchBase

class TwoDSearch(SearchBase):
    """
    A class for searching for a target element in a 2D matrix.
    """
    def search(self, matrix: List, target: int | float | str) -> int | float | str:
        """
        Search for a target element in the 2D matrix.

        Args:
            matrix (List[List[Union[int, float, str]]]): The 2D matrix to search in.
            target (Union[int, float, str]): The target element to search for.

        Returns:
            bool: True if the target element is found in the matrix, False otherwise.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        left, right = 0, (rows * columns) - 1
        if rows == 0:
            return False 
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid//columns][mid%columns]
            if target == mid_element:
                return True
            elif target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        
    
if __name__ == "__main__":
    linear_search = TwoDSearch()
    result = linear_search.search([[1,3,7,5], [10, 11, 16, 20], [23 , 30, 34, 60]], 3)
    print(result)