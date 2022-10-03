class Solution(object):
    def check(self,mydict):
        for val in mydict.values():
            if val != 1:
                return False
        return True
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        window_size = 0
        start = 0
        mydict = dict()
        while(start + window_size < size):
            #our window is s[start:window_size]
            #print("window: ", s[start: start + window_size])
            #print(mydict)
            if((s[start + window_size] not in mydict) and self.check(mydict)):
                #adding to window
                mydict[s[start + window_size]] = 1
                window_size += 1
            else:
                #moving window, addition
                if (s[start + window_size] not in mydict):
                    mydict[s[start + window_size]] = 1
                else:
                    mydict[s[start + window_size]] = mydict[s[start + window_size]] + 1
                #moving window, deletion
                if (mydict[s[start]] <= 1):#the start one will always be in dict so 1 is default value
                    #print("deleting,", s[start])
                    mydict.pop(s[start])
                else:
                    mydict[s[start]] = mydict[s[start]] - 1
                    
                start += 1
        return window_size
                
mySol = Solution()
#print(mySol.lengthOfLongestSubstring("abcabcbb"))
#print(mySol.lengthOfLongestSubstring("bbbbbb"))
print(mySol.lengthOfLongestSubstring("pwwkew"))