import player

def less(a, b):
    a = a.lower().replace('_', '')
    b = b.lower().replace('_', '')
    return a < b

def equal(a, b):
    a = a.lower().replace('_', '')
    b = b.lower().replace('_', '')
    return a == b

def binary_search(list, search_value, lo, hi):
    if (len(list) == 0):
        return -1
    else:
        middle = (hi + lo) // 2
        if equal(search_value, list[middle].get_full_name()):
            return middle
        elif (less(list[middle].get_full_name(), search_value)):
            result = binary_search(list, search_value, middle + 1, hi)
            if result == -1:
                return -1
            else:
                return middle + 1 + result
        elif (less(search_value, list[middle].get_full_name())):
            return binary_search(list, search_value, lo, middle - 1)
        
def continuous_search(list, search_value, lo, hi):
    for i in range(lo, hi + 1):
        if equal(search_value, list[i].get_full_name()):
            return i
    return -1