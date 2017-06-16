'''
Write a Python program to find the second smallest number in a list.
Define a function that takes a list of numbers as a parameter and returns the second smallest number in the list.
Example:

Input

[1, 2, -8, -2, 0]

Output

-2
'''
def solution(a_list):
    x = [x for x in sorted(a_list) if x!= min(a_list)]
    return x[0]
