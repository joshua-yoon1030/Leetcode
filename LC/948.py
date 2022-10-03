class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        score = 0
        possible = set()
        possible.add(0)
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1:
                possible.add(score)
                power += tokens[right]
                score -= 1
                right -= 1
        possible.add(score)
        return max(possible)
