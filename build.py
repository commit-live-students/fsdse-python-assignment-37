def solution(a_list):
    x = [x for x in sorted(a_list) if x!= min(a_list)]
    return x[0]
