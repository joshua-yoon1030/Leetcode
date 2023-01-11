#79: Word Search
#https://leetcode.com/problems/word-search/
#strategy: Run a dfs starting from the first letter of the word
#dfs from every spot there, and then have your visited list be differnet for every new word search
#if you complete the word, then you found it
#if you never complete the word, you don't found it
#runtime: O(n^2) to run the original scan, worst case we dfs O(n^2) on every square, so O(n^4)
#this is ok because n is like 6 lmfao
class Solution(object):
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        #method specifications:
        #visited: the visited set 
        #x, y: x and y of location on board
        #i: index of point we are in the word search
        def dfs(visited, x, y, i):
            if (x,y) in visited:
                return False
            if board[x][y] != word[i]:
                return False
            if i >= len(word) -1:
                return True
            
            #print("successfully found", word[i])
            visited.add((x,y))
            ans = False
            if x > 0:
                ans = ans or dfs(visited, x-1, y, i+1)
            if x < len(board)-1:
                ans = ans or dfs(visited, x+1, y, i+1)
            if y > 0:
                ans = ans or dfs(visited, x, y-1, i+1)
            if y < len(board[0])-1:
                ans = ans or dfs(visited, x, y+1, i+1)
            visited.remove((x,y))
            return ans


        word = list(word)
        ans = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    #print(i,j)
                    if len(word) == 1:
                        return True
                    ans = ans or dfs(set(), i, j, 0)
                    
        return ans

mySol = Solution()
print(mySol.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAABAA"))
