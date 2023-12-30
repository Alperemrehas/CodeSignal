'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''

def solution(n):    
    list_of_digits = [int(i) for i in str(n)]
    count = 0
    
    while len(list_of_digits) >= 2:
        _sum = 0  # Reset sum to 0 at the start of each iteration
        for i in list_of_digits:
            _sum += i
        list_of_digits = [int(i) for i in str(_sum)]
        count += 1

    return count

if __name__ == '__main__':
    result = solution(91)
    print(result)  # Output: 2
