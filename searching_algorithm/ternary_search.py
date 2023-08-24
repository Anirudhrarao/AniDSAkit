from typing import List, Union
from search_pkg.search_base import SearchBase

class TernarySearch(SearchBase):
    
    def search(self, arr: List, target: int | float | str) -> int | float | str:
        left, right = 0, len(arr) - 1 
        try:
            while left <= right:
                mid1 = left + (right - left) // 3
                mid2 = right - (right - left) // 3
                if target == arr[mid1]:
                    return mid1
                elif target == arr[mid2]:
                    return mid2
                elif target < arr[mid1]:
                    right = mid1 - 1
                elif target > arr[mid2]:
                    left = mid2 + 1
                else:
                    left = mid1 + 1
                    right = mid2 - 1
            return -1
        except Exception as e:
            raise e

if __name__ == "__main__":
    ternary_search = TernarySearch()
    result = ternary_search.search([1,2,3,4,5,6,7,8,9],5)
    print(result)