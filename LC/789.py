class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        target_dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_dist = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if ghost_dist <= target_dist:
                return False
        return True