class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        players = set()
        lost_once = set()
        lost_twice = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            if loser in lost_once:
                lost_twice.add(loser)
            lost_once.add(loser)
        winner_list = list(players.difference(lost_once))
        lost_once_list = list(lost_once.difference(lost_twice))
        winner_list.sort()
        lost_once_list.sort()
        return [winner_list, lost_once_list]

            