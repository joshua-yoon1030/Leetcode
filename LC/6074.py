class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        counter = 0
        for char in list(s):
            if char == letter:
                counter += 1
        percent = 100 * counter / len(s)
        return int(percent)
