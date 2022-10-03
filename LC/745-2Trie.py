import collections
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        #make the prefix and suffix trie
        self.trie1 = Trie()
        self.trie2 = Trie()
        for weight, word in enumerate(words): #enumerate just gets the index
            cur = self.trie1
            self.addw(cur, weight)
            #inserting word into prefix trie
            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            #inserting same word into suffix tree
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)
    
    #marks along the tree which indicies(words) are still in the tree
    def addw(self, node, w):
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cur1 = self.trie1
        #find the point in the tree where our prefix is
        for letter in prefix:
            if letter not in cur1: return -1
            else:
                cur1 = cur1[letter]
        
        #find the point in the tree where our suffix is
        cur2 = self.trie2
        for letter in suffix:
            if letter not in cur2: return -1
            else:
                cur2 = cur2[letter]
        
        #at this point, the dictionary entry [WEIGHT] should have
        #all the indicies of the words that have this prefix
        matches = cur1[WEIGHT] & cur2[WEIGHT]
        return max(matches)


        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)