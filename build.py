def solution(a_list):
    first_min = min(int(s) for s in a_list)
    a_list.remove(first_min)
    second_min = min(int(s) for s in a_list)
    return second_min

solution([1, 2, -8, -2, 0])
