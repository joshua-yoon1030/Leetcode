import collections
Trie = lambda: collections.defaultdict(Trie)

class Solution:
    
    def traverse(self, node, token):
        #node is a node in the trie
        #print(node.keys())

        if len(node) == 0:
            return [token]
        tokens = []
        for letter in node.keys():
            #print("traversing", letter)
            #tokens = []
            tokens += self.traverse(node[letter], token + letter)

        return tokens

    def minimumLengthEncoding(self, words):
        #generate trie
        self.trie = Trie()
        for word in words:
            cur = self.trie
            for letter in word[::-1]:
                #print("adding", letter)
                cur = cur[letter]
        
        #traverse trie
        encoding = self.traverse(self.trie, "")
        ans = 0
        encoding = [len(x) for x in encoding]
        ans += sum(encoding)
        return ans + len(encoding)
mySol = Solution()

print(mySol.minimumLengthEncoding(["time", "me", "bell"]))
        

