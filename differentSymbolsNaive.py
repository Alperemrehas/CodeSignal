'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

[output] integer
'''

def solution(s):
    list_chr = []
    for c in s:
        list_chr.append(c)
    return len(set(list_chr))

#OR

def solution_2(s):
    return len(list(set(s)))
