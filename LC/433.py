#433: Minimum Genetic Mutation
#https://leetcode.com/problems/minimum-genetic-mutation/
#Strategy: Create a graph of all the possible mutations that can occur
#eg. if you have ab -> ac, that would be an edge on the graph
#Then, if you run a bfs from the startgene, you can find how long it takes to get the target
#Else, it's impossible and return -1
#runtime, O(n^3) to build the graph, but there's only a max of 10 nodes lmfao
from collections import defaultdict
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def isOneapart(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
            return diff == 1

        def buildgraph(bank):
            wordbank = defaultdict(list)
            for word1 in bank:
                for word2 in bank:
                    if isOneapart(word1, word2):
                        wordbank[word1].append(word2)
                        wordbank[word2].append(word1)
            return wordbank
        def bfs(graph, visited, start, end):
            queue = []
            queue.append((start,0))

            while queue:
                (node, time) = queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    if node == end:
                        return time
                    for neighbor in graph[node]:
                        queue.append((neighbor, time + 1))
            
            #not found
            return -1
        bank.append(startGene)
        graph = buildgraph(bank)
        return bfs(graph, set(), startGene, endGene)


        