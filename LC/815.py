from collections import defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        routes = list(map(set, routes))
        transfers = defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes)):
                if i != j and len(routes[i].intersection(routes[j])) > 0:
                    transfers[i].add(j)
        
        visited_stops = set()
        visited_routes = set()
        visited_stops.add(source)
        buses = 0
        prev = 0
        prev_routes = set()
        prev_stops = set()
        for i in range(len(routes)):
            if source in routes[i]:
                visited_routes.add(i)
                prev_routes.add(i)
        
        #print(transfers)
        
        while prev != len(visited_stops):
            #print("buses, visited_stops, visited_routes: ", buses, visited_stops, visited_routes)
            prev = len(visited_stops)
            if target in visited_stops:
                return buses
            buses += 1
            prev_stops = set()
            for neighbor in prev_routes:
                visited_stops = visited_stops.union(routes[neighbor])
                prev_stops = prev_stops.union(routes[neighbor])
        
            temp = set()
            for route in prev_routes:
                for transfer in transfers[route]:
                    if transfer not in visited_routes:
                        visited_routes.add(transfer)
                        temp.add(transfer)
            prev_routes = temp
        
        return -1