from collections import deque
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numstack = deque()
        opstack = deque()
        s = s.replace(" ", "")
        i = 0

        def nextNum(s, i):
            num = "1234567890"
            myNum = ""
            while i < len(s) and s[i] in num:
                myNum += s[i]
                i += 1
            return (int(myNum), i)

        while i < len(s):
            num, i = nextNum(s, i)
            numstack.appendleft(num)
            if i == len(s):
                break
                
            opstack.appendleft(s[i])
            i += 1
            if opstack[0] == "*" or opstack[0] == "/":
                num1, i = nextNum(s, i)
                num2 = numstack.popleft()
                if opstack[0] == "*":
                    numstack.appendleft(num1 * num2)
                else:
                    numstack.appendleft(num2 // num1)
                opstack.popleft()
            
        while len(opstack) > 0:
            num2 = numstack.popleft()
            num1 = numstack.popleft()
            op = numstack.popleft()
            if op == "+":
                numstack.appendleft(num1 + num2)
            else:
                numstack.appendleft(num1 - num2)
        return numstack[0]

        
        




        