import player

def less(a, b):
    a = a.lower().replace('_', '')
    b = b.lower().replace('_', '')
    return a < b

def equal(a, b):
    a = a.lower().replace('_', '')
    b = b.lower().replace('_', '')
    return a == b
'''
This function is made to order the name of player.
'''
def continuous_search(list, search_value, lo, hi):
    for i in range(lo, hi + 1):
        if equal(search_value, list[i].get_full_name()):
            return i
    return -1
