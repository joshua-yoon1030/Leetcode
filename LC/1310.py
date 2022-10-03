class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #setup of prefix xor array
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = arr[i] ^ prefix[i-1]
        
        #generate queries
        ans = [0] * len(queries)
        count = 0
        for start, end in queries:
            if start == 0:
                ans[count] = prefix[end]
            else:
                ans[count] = prefix[end] ^ prefix[start-1]
            count += 1
        return ans
