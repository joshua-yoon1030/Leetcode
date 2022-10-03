class Solution(object):
    def __init__(self):
        self.memo = dict()
    def minimumRounds(self, tasks):
        task_dict = dict()
        for num in tasks:
            if (task_dict.get(num) != None):
                task_dict[num] = task_dict.get(num) + 1
            else:
                task_dict[num] = 1

        minimum = 0
        for value in task_dict.values():
            if(value  == 1):
                return -1
            else:
                minimum = minimum + optimalFill(value)
        return minimum
    

    def optimalFill(self, n):
        if(n == 0):
            return 0
        elif(n <= 1):
            return 34738723894
        elif(n == 2):
            return 1
        elif(self.memo.get(n) != None):
            return self.memo.get(n)
        else:
            a = optimalFill(n-2) + 1
            b = optimalFill(n-3) + 1
            self.memo[n] = min(a,b) + 1
            return self.memo[n]
            
        