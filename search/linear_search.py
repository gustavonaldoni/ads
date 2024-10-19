def linear_search(array: list, element: int) -> int:
    for i, el in enumerate(array):
        if el == element:
            return i
    
    return -1