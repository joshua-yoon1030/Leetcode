#658. Find K closest Elements
#https://leetcode.com/problems/find-k-closest-elements/
#My Strategy: You have to favor the smaller numbers.
#Therefore, I will make all numbers smaller than x closer to x by 0.5
#that way, I still preserve rule 1: (eg. 6 is closer to 5 than 3.5)
#but also, I preserve rule 2: (eg. 6 is farther to 5 then 4.5)
#then I subtract everything by x and abs value it, then sort the array
#I take the first k numbers, then go through and change it back
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        for i in range(len(arr)):
            if arr[i] < x:
                arr[i] = abs(0.5 + arr[i] - x)
            else:
                arr[i] -= x
        arr.sort()
        ans = arr[:k]
        for i in range(len(ans)):
            if isinstance(ans[i], float):
                ans[i] = int(x -0.5 - ans[i] )
            else:
                ans[i] += x
        ans.sort()
        return ans 


        