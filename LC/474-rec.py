def stringRead(text):    
#general string reading, converts "00110" -> (3,2)    
        x, y = 0,0       
        for t in text:
            if t == '0':
                x += 1
            else:
                y += 1
        return (x,y)
def recurse(strs, index, m, n):
    if index == len(strs):
        return 0
    elif(m == 0 and n == 0):
        return 0
    
    (numZ, numO) = strs[index]
    #if we go under 0 dont use for sure
    if (m - numZ < 0 or n - numO < 0):
        return recurse(strs, index + 1, m, n)
    
    #let's try using strs[index] in our sol
    used = 1 + recurse(strs, index + 1, m - numZ, n - numO)
    #what if we don't use it?
    unused = 0 + recurse(strs, index + 1, m, n)

    #which one worked better?
    return max(used, unused)

def findMaxForm(strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        mapped = map((stringRead), strs)
        #converts "00110" -> (3,2)  
        strs = list(mapped)

        res = recurse(strs,0, m, n)
        return res
print(findMaxForm(["10","0","1"], 1, 1))
print(findMaxForm(["10","0001","111001","1","0"], 5, 3))
print(findMaxForm(["10","0001","111001","1","0"],4,3))
print(findMaxForm(["011111","001","001"], 4, 5))