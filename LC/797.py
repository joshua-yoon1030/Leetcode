from collections import deque
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        def traverse(node, stack, ans):
            if node == len(graph) - 1:
                stack.append(node)
                ans.append(list(stack))
                stack.pop()
                return
            #print("appending", node)
            stack.append(node)
            for neighbor in graph[node]:
                traverse(neighbor, stack, ans)
            stack.pop()
            return 
        
        stack = deque()
        ans = []
        traverse(0, stack, ans)
        return ans
