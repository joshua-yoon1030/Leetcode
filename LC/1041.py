#1041: Robot Bounded in Circle
#Strategy: The robot can only be contained in a circle if the instructions make him return to the origin.
#Just simulate the instructions, and see if you end at the origin, or you are facing a non north direction.
#runtime: O(n) where n is the len(instructions)
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x = 0
        y = 0
        dirx = [0,1,0,-1]
        diry = [1,0,-1,0]
        i = 0
        for letter in instructions:
            if letter == "G":
                x += dirx[i]
                y += diry[i]
            elif letter == "L":
                i = (i-1)%4
            elif letter == "R":
                i = (i+1) %4
        
        if x == 0 and y == 0:
            return True
        elif i != 0:
            return True
        return False
        