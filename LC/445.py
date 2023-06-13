# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def traverse(n1, n2, head1, head2):
            if not n1 and not n2:
                return (head1, head2)
            if n1 and n2:
                n1 = n1.next
                n2 = n2.next
                return traverse(n1, n2, head1, head2)
            elif n1:  
                temp = ListNode(0, head2)
                temp.next = head2
                return traverse(n1.next, n2, head1, temp)
            elif n2:
                temp = ListNode(0, head1)
                temp.next = head1
                return traverse(n1, n2.next, temp, head2)
        
        num1, num2 = traverse(l1, l2, l1, l2)

        def add(n1, n2):
            if not n1 and not n2:
                return (None, 0)
            (ans, carry) = add(n1.next, n2.next)
            return (ListNode((carry + n1.val + n2.val) % 10, ans), (carry + n1.val + n2.val) // 10)

        (ans, carry) = add(num1, num2)
        if carry > 0:
            return ListNode(1, ans)
        return ans