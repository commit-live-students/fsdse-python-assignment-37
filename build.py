a_list=[1, 2, -8, -2, 0]
b_list=[]
def solution(a_list):
    first_min=min(a_list)
    a_list.remove(first_min)
    sec_min=min(a_list)
    return sec_min
solution(a_list)
