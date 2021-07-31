"""
50. Pow(x, n)
Medium

https://leetcode.com/problems/powx-n/


Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

Accepted    Submissions
679,272     2,163,590
"""


def myPow(x: float, n: int) -> float:
    """
    Runtime: 24 ms, faster than 96.07% of Python3 online submissions for Pow(x, n).
    Memory Usage: 14.2 MB, less than 79.22% of Python3 online submissions for Pow(x, n).

    
    """
    if not n:
        return 1
    if n == -1:
        return 1 / x
    p = powpow(x, n // 2)
    return p * p if n % 2 == 0 else x * p * p


if __name__ == '__main__':
    print(-3//2)