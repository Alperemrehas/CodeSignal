'''Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.'''

def solution(n):
    return all(int(item) % 2 == 0 for item in str(n))
