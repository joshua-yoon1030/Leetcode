from collections import deque
class MinStack(object):

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.push(val)
        if self.minstack[0] >= val:
            self.minstack.push(val) 
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[0] == self.minstack[0]:
            self.minstack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()