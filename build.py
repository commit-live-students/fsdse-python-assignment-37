def solution(a_list):
    second_smallest = [second_smallest for second_smallest in sorted(a_list) if second_smallest!= min(a_list)]
    return second_smallest[0]
