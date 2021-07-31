"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

https://leetcode.com/problems/merge-k-sorted-lists/

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

Accepted    Submissions
945,561     2,144,314
"""


# Definition for singly-linked list.
class ListNode:
    # noinspection PyShadowingBuiltins
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(arr):
    # print(f'arr = {arr}')
    if not arr:
        return None
    node = ListNode(arr[0])
    node.next = make_list(arr[1:])
    return node


# noinspection PyShadowingNames
def print_list(l):
    if not l:
        return
    print(str(l.val) + '->')
    print_list(l.next)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def comp(p, q):
    return p.val < q.val


def comp_and_swap(p, q):
    (p, q) = (p, q) if comp(p, q) else (q, p)
    return p, q


# noinspection PyShadowingNames
def merge_2_lists(l, h):
    if not h:
        return l
    if not l:
        return h
    s = l
    l = l.next
    if l:
        l, h = (l, h) if comp(l, h) else (h, l)
    s.next = merge_2_lists(l, h)
    return s


def merge_k_lists_rec(ll):
    if not ll:
        return None
    if len(ll) < 2:
        return ll[0]
    ll[0], ll[1] = comp_and_swap(ll[0], ll[1])
    p, q = merge_2_lists(ll[0], ll[1]), merge_k_lists_rec(ll[2:])
    if p and q:
        p, q = comp_and_swap(p, q)
    return merge_2_lists(p, q)


if __name__ == '__main__':
    pass