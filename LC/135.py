#135: Candy
#Strategy: Traverse the array, and update on how much extra candy you need to give
#If you go from a higher rating to a lower rating, reset to 0 extra candy
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = 0
        lastzero = 0
        goingup = False
        ratingstack = 9999999
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i-1] and goingup:
                #the rating went down while we are going up, we can reset to 0 candies
                goingup = False
                #print("no candy added")
                lastzero = i
            elif ratings[i] < ratings[i-1]:
                #the rating went down while we were going down
                #print("adding", i-lastzero, " candy")
                candy += i - lastzero
                if i-lastzero >= ratingstack:
                    #print("adding extra")
                    candy += 1
            elif ratings[i] > ratings[i-1] and not goingup:
                ratingstack = 1
                #print("adding", ratingstack, " candy")
                candy += ratingstack
                goingup = True
            elif ratings[i] > ratings[i-1]:
                ratingstack += 1
                #print("adding", ratingstack, " candy")
                candy += ratingstack
            else:
                #the rating is the same, we have to assume we are going down now
                goingup = False
                lastzero = i
                ratingstack = 9999999
        return candy + len(ratings)
            

        