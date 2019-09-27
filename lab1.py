def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError("No")

    if not int_list:
        return None

    max_num = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max_num:
            max_num = int_list[i]
    return max_num


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError("No")

    if len(int_list) == 0:
        return []

    return [int_list[-1]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    mid = len(int_list)//2

    if int_list is None:
        raise ValueError()

    if len(int_list) == 0:
        return None

    if target == int_list[mid]:
        return mid

    if target < int_list[mid]:
        high = mid - 1
        return bin_search(target, low, high, int_list[:mid])

    elif target > int_list[mid]:
        low = mid + 1
        return bin_search(target, low, high, int_list[mid+1:])


# if __name__ == "__main__":
#     list1 = [12, 5, 7]
#     print(reverse_rec(list1))
