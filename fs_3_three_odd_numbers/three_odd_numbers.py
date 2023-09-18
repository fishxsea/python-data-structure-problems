def add_one(nums):
    '''adds 1 to every number in the list'''
    return [i + 1 for i in nums]

def three_odd_numbers(nums=[]):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    
    pool = [0, 1, 2]
    for _ in range(len(nums)):
        if pool[-1] == len(nums):
            break
        n = [nums[i] for i in pool]
        if sum(n) % 2 != 0:
            return True
        pool = add_one(pool)
    return False
    
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))