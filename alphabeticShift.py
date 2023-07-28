def solution(inputString):
    new_string=''
    for i in range(len(inputString)):        
        ca = chr(ord(inputString[i])+1)
        if ca > 'z':
            new_string=new_string+'a'
        else:    
            new_string=new_string + ca
    return new_string
'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
'''

