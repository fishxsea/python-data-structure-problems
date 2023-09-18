def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    
    list_items = all(isinstance(li, list) for li in lst)
    if list_items:
        return True
    return False
    
print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
