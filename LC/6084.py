import collections
class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        messageDict = collections.defaultdict(int)
        for i in range(len(messages)):
            name = senders[i]
            messageLength = len(messages[i].split(" "))
            messageDict[name] += messageLength
        largest = 0
        largest_name = ""
        for i in messageDict.keys():
            if messageDict[i] > largest:
                largest_name = i
                largest = messageDict[i]
            elif(messageDict[i] == largest):
                if largest_name < i:
                    largest_name = i
                    largest = messageDict[i]
        return largest_name
mySol = Solution()
print(mySol.largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"]))
print(mySol.largestWordCount(["a", "a"],["bob","charlie"]))