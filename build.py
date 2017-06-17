def solution(a_list):
    min1 = a_list[0]
    min1sub = 0
    min2 = a_list[0]
    min2sub = 0
    for i in range(len(a_list)):
        if min1>a_list[i]:
            min1 = a_list[i]
            min1sub = i
    for j in range(len(a_list)):
        if (min2>a_list[j] and j!=min1sub):
            min2 = a_list[j]
            min2sub = j
    print("Minimum is ",min1,"at index",min1sub)
    print("Second lowest is ",min2,"at index ",min2sub)
    return min2
"""This solution uses 2 for-loops,
Alternatively you could simply sort the given list ascendingly
 and return the 0th(lowest) and 1st(2nd lowest) elements,though this would be n^2."""

solution([23,43,64,7,0])
