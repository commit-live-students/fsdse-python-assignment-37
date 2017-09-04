def solution(a_list):
    m1,m2 = float('inf'), float('inf')
    for x in a_list:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2
print solution([1, 2, -8, -2, 0])
