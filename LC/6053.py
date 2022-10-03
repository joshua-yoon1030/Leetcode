class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        guard_x = dict()
        wall_x = dict()
        guard_y = dict()
        wall_y = dict()
        for [x,y] in guards:
            if(guard_x.get(x) != None):
                guard_x.get(x).append(y)
            else:
                guard_x[x] = [y]
            if(guard_y.get(y) != None):
                guard_y.get(y).append(x)
            else:
                guard_y[y] = [x]
        for [x,y] in walls:
            if(wall_x.get(x) != None):
                wall_x.get(x).append(y)
            else:
                wall_x[x] = [y]
            if(wall_y.get(y) != None):
                wall_y.get(y).append(x)
            else:
                wall_y[y] = [x]
        
        for x in range(m):
            for y in range(n):
                #point is [x,y]
                guard_list_x = guard_x.get(x)
                wall_list_x = wall_x.get(x)
                guard_list_y = guard_y.get(y)
                wall_list_y = wall_y.get(y)
                if(wall_list_x == None and guard_list_x != None):
                    #caught
                    continue
                elif(wall_list_x == None and guard_list_x == None):
                    #have to keep checking
                    pass
                elif(wall_list_x != None and guard_list_x == None):
                    #have to keep checking
                    pass
                else:
                    g1 = guard_list_x - y
                    w1 = wall_list_x - y
                    
                    

            
        