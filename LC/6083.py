class Solution(object):
    def digitCount(self, num):
        num = list(num)
        for i in range(len(num)):
            counter = 0
            digit_to_count = i
            for j in num:
                #print("digit to Count, ", i, "looking at ", j)
                if str(i) == j:
                    #print("hi")
                    counter += 1
            if str(counter) != num[i]:
                return False
        return True
        


mySol = Solution()
print(mySol.digitCount("1210"))
print(mySol.digitCount("030"))

        