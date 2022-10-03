class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        consider = True
        count = 0
        for letter in s:
            if letter == "|":
                consider = not consider
            elif letter == "*" and consider:
                count += 1
        return count
mySol = Solution()
print(mySol.countAsterisks("l|*e*et|c**o|*de|"))
print(mySol.countAsterisks("iamprogrammer"))
print(mySol.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))