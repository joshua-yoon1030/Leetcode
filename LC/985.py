#we keep a evenSum, and depending on what happens, we change our evenSum accordingly
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #setup
        evenSum = 0
        for num in nums:
            if num %2 == 0:
                evenSum += num

        ans = []
        for query in queries:
            index = query[1]
            addme = query[0]
            if nums[index] %2 == 0 and addme %2 == 0:
                #if the org number is even and the query is even,
                #we need to update the sum by addme
                evenSum += addme
            elif nums[index] %2 == 0 and addme %2 == 1:
                #our even number turned into an odd number
                evenSum -= nums[index]
            elif nums[index] %2 == 1 and addme%2 == 1:
                #our odd number turned into an even number
                evenSum += nums[index]
                evenSum += addme
            #odd turning into odd has no effect
            nums[index] += addme
            ans.append(evenSum)
        return ans
