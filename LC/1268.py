import collections
Trie = lambda:collections.defaultdict(Trie)
class Solution(object):
    def traverseTree(self, node, build):
        if len(node) == 0:
            return [build]
        final = []
        for key in node.keys():
            if key == '#':
                final += [build]
            else:
                final +=(self.traverseTree( node[key], build+key))

        return final

    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        #generate Trie
        self.trie = Trie()
        for word in products:
            cur = self.trie
            for letter in word:
                cur = cur[letter]
            cur['#'] = True
        
        ans = []
        for i in range(len(searchWord)):
            cur = self.trie
            build = ""
            flag = False
            #first traverse tree for i steps
            for j in range(0,i+1):
                if searchWord[j] not in cur:
                    ans.append([])
                    print(searchWord[j])
                    flag = True
                    break
                else:
                    cur = cur[searchWord[j]]
                    build += searchWord[j]
            if flag: continue
            i_list = self.traverseTree(cur, build)
            i_list.sort()
            if (len(i_list) < 4):
                ans.append(i_list)
            else:
                ans.append(i_list[:3])
        
        return ans
mySol = Solution()
print(mySol.suggestedProducts(["havana"], "tatiana"))
#print(mySol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))

        