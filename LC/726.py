from collections import defaultdict
from collections import deque
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        #begin parsing library
        def extractName(formula, i):
            #reads the formula starting at i (inclusive) and parses the next element name.
            #returns (name, j), where j is the index of next unread character
            element = formula[i]
            lower = "abcdefghijklmnopqrstuvwxyz"
            i += 1
            while i < len(formula) and formula[i] in lower:
                element += formula[i]
                i += 1
            return element, i
        
        def extractNumber(formula, i):
            #reads the formula starting at i and parses next number
            #returns (num, j), where num is an int, and j is index of next unread
            num = "1234567890"
            if i >= len(formula) or formula[i] not in num:
                #wasn't a number to begin with
                return (1, i)
        
            number = formula[i]
            i += 1
            while i < len(formula) and formula[i] in num:
                number += formula[i]
                i += 1
            return int(number), i
        
        def parseAnswer(chemicals):
            #takes in a dictionary of chemicals and makes it into answer format
            ans = ""
            for name, num in sorted(list(chemicals.items())): #?...
                ans += name
                if num > 1:
                    ans += str(num)
            return ans
        #end parsing library
        
        i = 0
        chemicals = defaultdict(lambda: 0)
        chemstack = deque()

        while i < len(formula):
            if formula[i] == "(":
                chemstack.append("(")
                i += 1
            elif formula[i] == ")":
                mult, i = extractNumber(formula, i+1)
                tempstack = deque()
                while chemstack[-1] != "(":
                    #safe bc valid sequences always have a ( before a )
                    tempstack.append(chemstack.pop())
                chemstack.pop()
                while len(tempstack) > 0:
                    (chem, atoms) = tempstack.pop()
                    chemstack.append((chem, atoms * mult))
            else:
                name, i = extractName(formula, i)
                num, i = extractNumber(formula, i)
                chemstack.append((name, num))
        while len(chemstack) > 0:
            name, num = chemstack.pop()
            chemicals[name] += num
        return parseAnswer(chemicals)

mySol = Solution()
print(mySol.countOfAtoms("MgO2H2"))
