def solution(a_list):
    """Enter Code Here"""
    #lst = a_list.copy()
    #x = lst.remove(min(lst))
    #return min(a_list)
    return sorted(a_list)[1]


d = [1, 2, -8, -2, 0]
print solution(d)
