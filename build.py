def solution(a_list):
    """This contains two steps:
    1: sort the list
    2: as list is in sorted order check for the 2nd item of the same to get the second highest value

    """
    a_list.sort()
    print a_list[1]
    return a_list[1]

solution([1, 2, -8, -2, 0])
