from collections import defaultdict
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        graph = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i > 0:
                    graph[(i,j)].append((i-1, j))
                if i < len(board) - 1:
                    graph[(i, j)].append((i + 1, j))
                if j > 0:
                    graph[(i,j)].append((i, j-1))
                if j < len(board[0]) - 1:
                    graph[(i, j)].append((i, j + 1))
        #print(graph)
        
        self.visited = set()
        def dfs(x, y, i):
            if i >= len(word) or len(word) == 1:
                return True
            if (x,y) in self.visited:
                return False
            if board[x][y] != word[i]:
                
                return False

            self.visited.add((x,y))

            search = False
            for a, b in graph[(x,y)]:
                #print("dfs from:", x, y, " to: ", a, b)
                search = search or dfs(a,b, i + 1)
            self.visited.remove((x,y))
            return search
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:            
                    self.visited = set()
                    if(dfs(i, j, 0)):
                        return True
        return False

            


        