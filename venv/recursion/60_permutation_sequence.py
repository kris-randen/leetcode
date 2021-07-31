"""
60. Permutation Sequence
Hard

https://leetcode.com/problems/permutation-sequence/

2594

375

Add to List

Share
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.



Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"


Constraints:

1 <= n <= 9
1 <= k <= n!
"""

from math import factorial


# noinspection PyShadowingNames
def get_index_elem(n, ind, d):
    c = 0
    i = 0
    while c < d:
        while i in ind:
            i += 1
        i += 1
        c += 1
    while i in ind:
        i += 1
    e = i+1
    return i, e


# noinspection PyShadowingNames
def perm_seq_recur(n, k, ind):
    """
    :param n: max number for the increasing sequence 1, 2, 3, ... n
    :param k: the kth element of the sorted list of permutations that's being sought
    :param ind: list of indices that have appeared in the prefix
    :return: kth element of the sorted list of permutations of 1, 2, .. n devoid of ind

    Runtime: 24 ms, faster than 96.72% of Python3 online submissions for Permutation Sequence.
    Memory Usage: 14.3 MB, less than 69.65% of Python3 online submissions for Permutation Sequence.

    """
    if k == 1:
        return ''.join([str(j) if j - 1 not in ind else '' for j in range(1, n + 1)])
    m = n - len(ind)
    fact = factorial(m - 1)
    d = k // fact
    r = k % fact
    d = d if r != 0 else d - 1
    r = r if r != 0 else fact
    d, s = get_index_elem(n, ind, d)
    ind.append(d)
    return str(s) + perm_seq_recur(n, r, ind)


def perm_seq_recursive(li, k):
    """
    :param li:
    :param k:
    :return:

    Runtime: 24 ms, faster than 96.72% of Python3 online submissions for Permutation Sequence.
    Memory Usage: 14.5 MB, less than 17.51% of Python3 online submissions for Permutation Sequence.
    """
    if k == 1:
        return ''.join([str(j) for j in li])
    n = len(li)
    fact = factorial(n-1)
    d = k // fact
    r = k % fact
    d = d if r != 0 else d - 1
    r = r if r != 0 else fact
    s = li[d]
    li.pop(d)
    return str(s) + perm_seq_recursive(li, r)


def getPermutation(n: int, k: int) -> str:
    return perm_seq_recur(n, k, [])


if __name__ == '__main__':
    perm = getPermutation(4, 2)
    print(perm)