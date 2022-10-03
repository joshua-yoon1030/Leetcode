# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#143. reorder list:
#strategy: Put all the nodes into a list first, then pop them off from the front and back
#repeat until empty
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        cur = head
        nodeList = []
        while cur:
            nodeList.append(cur)
            cur = cur.next
        
        #print(nodeList)
        parity = 1
        head = nodeList.pop(0)
        cur = head
        while nodeList:
            if parity %2 == 0:
                #print("popping", nodeList[0])
                cur.next = nodeList.pop(0)
            else:
                #print("popping", nodeList[-1])
                cur.next = nodeList.pop(-1)
            cur = cur.next
            parity += 1
        cur.next = None
        return
            

        