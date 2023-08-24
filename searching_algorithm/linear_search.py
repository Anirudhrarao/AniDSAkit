from typing import List
from search_pkg.search_base import SearchBase

class LinearSearch(SearchBase):
    """
    Linear search algorithm implementation.

    This class provides an implementation of the linear search algorithm.
    It inherits from the SearchBase abstract class and defines the search method
    to perform a linear search in a list.

    Attributes:
        None
    """
    def search(self, arr: List, target: int | float | str) -> int | float | str:
        """
        Perform a linear search for a target element in a list.

        Args:
            arr (List[Union[int, float, str]]): The list to search within.
            target (Union[int, float, str]): The target element to search for.

        Returns:
            Union[int, float, str]: If the target is found, a string indicating
            the target value and its index is returned. If not found, a string
            indicating that the target value was not found and the index is -1 is returned.
        """
        try:
            for i in range(len(arr)):
                if arr[i] == target:
                    return f"The target value {target} found at index no: {i}"
            return f"The target value {target} not found, index: {-1}"
        except Exception as e:
            return f"Error: {str(e)}"
        
    
if __name__ == "__main__":
    linear_search = LinearSearch()
    result = linear_search.search([1, 2, 3, 4, 5], 3)
    print(result)