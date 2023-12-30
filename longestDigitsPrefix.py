'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
'''

def solution(inputString):
    new_str = ""
    for i in inputString:
        if i.isdigit():
            new_str = new_str + i
        else:
            return new_str
    return new_str