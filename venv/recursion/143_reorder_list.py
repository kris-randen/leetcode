"""
143. Reorder List
Medium

https://leetcode.com/problems/reorder-list/

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

Accepted    Submissions
348,475     816,624
"""


# Definition for singly-linked list.
class ListNode:
    # noinspection PyShadowingBuiltins
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'node: ' + str(self.val)

    def __iter__(self):
        return ListNodeIterator(self)


class ListNodeIterator:
    def __init__(self, node):
        self.node = node
        self.index = 0

    # noinspection PyShadowingNames
    def __next__(self):
        if not self.index:
            node = self.node
            # self.node = node.next
            self.index += 1
            return node
        if self.node.next:
            node = self.node
            self.node = node.next
            self.index += 1
            return node.next
        raise StopIteration


# noinspection PyShadowingNames
def make_list(values):
    if not values:
        return None
    node = ListNode(values[0])
    node.next = make_list(values[1:])
    return node


def reverse(lhead):
    """
    Note that for reversing without changing the original
    list we need to stay two hops away from the values.
    And therefore we use the values for the reverse list
    nodes (ListNode(node)) as the node of the original list.
    :param lhead:
    :return:
    """
    if not lhead.val.next:
        return lhead
    tail = lhead
    lnext = ListNode(lhead.val.next)
    pony = reverse(lnext)
    lnext.next = tail
    return pony


def reorderRecursive(head, ltail):
    """
    Reverse the list. Start with 1 and ListNode(n)
    connect 1 to n, n to 2 and then recurse by repeating
    on 2 and ListNode(n-1). Two cases arise:

    1. n is odd in which case the head and ltail will
    meet exactly at the center and therefore the base case
    for that will be head == ltail.val. Note that we also
    need to set the next node of head and ltail.val to None
    else we'll have a circular list.

    2. n is even in which case the head.next and ltail.val will
    meet at the bifocal center and therefore the base case for
    this will be head.next == ltail.val and we need to set
    ltail.val.next = None to avoid circularity

    :param head:
    :param ltail:
    :return:
    """
    print(f'head = {head}, ltail = {ltail}')
    if head == ltail.val:
        head.next = None
        return
    if head.next == ltail.val:
        ltail.val.next = None
        return

    hnext = head.next
    ltnext = ltail.next

    head.next = ltail.val
    ltail.val.next = hnext
    reorderRecursive(hnext, ltnext)


# noinspection PyShadowingNames
def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    ltail = reverse(ListNode(head))
    reorderRecursive(head, ltail)


if __name__ == '__main__':
    l = make_list([1, 2, 3, 4, 5, 6, 7])
    reorderList(l)

    for node in l:
        print(node)

    l = make_list([1, 2, 3, 4])
    reorderList(l)

    for node in l:
        print(node)