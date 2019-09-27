def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:  # test None and raise valueError
        raise ValueError()

    if not int_list:  # test if list is empty
        return None

    max_num = int_list[0]
    for i in range(len(int_list)):  # run through each item in list and comparing them to max
        if int_list[i] > max_num:
            max_num = int_list[i]
    return max_num


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:  # test None and raise valueError
        raise ValueError()

    if len(int_list) == 0:  # test if list is empty
        return []

    return [int_list[-1]] + reverse_rec(int_list[:-1])  # pulling the last item in list to the front


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = len(int_list)//2

    if int_list is None:  # test None and raise valueError
        raise ValueError()

    if len(int_list) == 0:  # test if list is empty
        return None

    if target == int_list[mid]:  # base case if target is found
        return mid

    if target < int_list[mid]:  # change high if target is less than mid
        high = mid - 1
        return bin_search(target, low, high, int_list[:mid])

    elif target > int_list[mid]: # change low if target is greater than mid
        low = mid + 1
        return bin_search(target, low, high, int_list[mid+1:])


