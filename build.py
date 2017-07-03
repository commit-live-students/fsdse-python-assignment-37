def solution(a_list):
    """Enter Code Here"""
    first_min  = min(a_list)
    print first_min
    a_list.remove(first_min)
    second_min = min(a_list)
    return second_min
