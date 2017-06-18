def solution(a_list):
    """Enter Code Here"""
    x = min(a_list)
    a_list.remove(x)
    y = min(a_list)
    return y
