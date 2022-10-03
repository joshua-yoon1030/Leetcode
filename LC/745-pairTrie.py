import collections
import itertools
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()

        for weight, word in enumerate(words):
            #adding in "apple" to pairTrie
            cur = self.trie
            cur[WEIGHT] = weight

            #add the rest of the prefixes in word
            #eg. [a, none] then, [p, none], then [p, none], etc.
            for i, x in enumerate(word):
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                #same but in reverse for suffixes
                #eg. [none, e] then [none, l], etc.
                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight
                
                #adding in the actual case
                #eg. [a, e]
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight
        

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cur = self.trie
        iterate = itertools.zip_longest(prefix, suffix[::-1])
        for a, b in iterate:
            if (a,b) not in cur:
                return -1
            else:
                cur = cur[(a,b)]
        return cur[WEIGHT]

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
word = "abc123"
i = 1
prefix = "abc123"
suffix = "asdf"
for a,b in (prefix, suffix[::-1]):
    print(a,b)
