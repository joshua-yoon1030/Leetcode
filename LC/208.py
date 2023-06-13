
class Trie(object):

    def __init__(self):
        self.trie = dict()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.trie
        for i in word:
            if i not in cur:
                cur[i] = dict()
            cur = cur[i]
        cur["#"] = dict()
        #print(self.trie)
    
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.trie
        for i in word:
            #print(cur.keys())
            if i not in cur:
                return False
            cur = cur[i]
        if "#" in cur:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.trie
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)