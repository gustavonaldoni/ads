def binary_search(array: list, element: int) -> int:
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if array[middle] == element:
            return middle
        
        elif array[middle] < element:
            left = middle + 1
        
        else:
            right = middle - 1
    
    return -1
