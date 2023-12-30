'''Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.'''

def solution(inputArray, k):
    max_sum = sum(inputArray[:k])  # Initialize max_sum with the sum of the first k elements
    current_sum = max_sum

    # Iterate through the array using a sliding window
    for i in range(k, len(inputArray)):
        # Update the current_sum by adding the next element and subtracting the first element of the window
        current_sum = current_sum + inputArray[i] - inputArray[i - k]
        # Update max_sum if the current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum


