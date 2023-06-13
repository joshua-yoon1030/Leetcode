# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #step 1: find the middle using the tortise hare alg.
        def firsttraverse(slow, fast):
            
            if not fast:
                return slow
            if not fast.next:
                return slow

            return firsttraverse(slow.next, fast.next.next)
        
        #step 2: Reversing the orientation of the back half of the ll
        prev = firsttraverse(head, head)
        
        cur = prev.next
        prev.next = None

        def changing(prev, cur):
            if not cur:
                return prev
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            return changing(prev, cur)
        
        backnode = changing(prev, cur)

        #step 3: Checking the palindrome: start from head and the back and skip next
        def check(front, back):
            if not front:
                return True
            if not back:
                return True
            if front.val != back.val:
                return False
            return check(front.next, back.next)

        return check(head, backnode)




            

                
 
            
                