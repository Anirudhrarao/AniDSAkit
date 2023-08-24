from typing import List, Union
from search_pkg.search_base import SearchBase

class BinarySearch(SearchBase):
    """
    Binary search algorithm implementation.

    This class provides an implementation of the binary search algorithm.
    It inherits from the SearchBase abstract class and defines the search method
    to perform a binary search in a sorted list.

    Attributes:
        None
    """
    def search(self, arr: List, target: int | float | str) -> int | float | str:
        """
        Perform a binary search for a target element in a sorted list.

        Args:
            arr (List[Union[int, float, str]]): The sorted list to search within.
            target (Union[int, float, str]): The target element to search for.

        Returns:
            int | float | str: If the target is found, the index of the target is returned.
            If not found, a string indicating that the target value was not found is returned.
        """
        start, end = 0, len(arr) - 1
        mid_index = start + (end - start) // 2
        try:
            while start <= end:
                mid_index = start + (end - start) // 2
                if arr[mid_index] == target:
                    return f"The target value {target} found at index no: {mid_index}"
                elif arr[mid_index] < target:
                    start = mid_index + 1
                else:
                    end = mid_index - 1
            return f"The target value {target} not found, index: -1"
        except Exception as e:
            return f"Error: {str(e)}"
            

if __name__ == "__main__":
    binary_search = BinarySearch()
    result = binary_search.search([1, 2, 3, 4, 5], 32)
    print(result)