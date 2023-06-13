from collections import deque
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        remove = set()
        word = s
        paren = deque()
        for i in range(len(word)):
            #print(word[i])
            if word[i] == '(':
                #print("add")
                paren.appendleft(i)
            elif word[i] == ')':
                #print("remove")
                if len(paren) > 0:
                    paren.popleft()
                else:
                    remove.add(i)
        while len(paren) > 0:
            remove.add(paren.pop())
        output = list()
        
        #print(remove)
        for i in range(len(word)):
            if i not in remove:
                output.append(word[i])
        return "".join(output)