
from cgitb import small


def smallestStringWithSwaps(s, pairs):
    """
    :type s: str
    :type pairs: List[List[int]]
    :rtype: str
    """
    notDone = True
    s = list(s)
    sr = s[::-1]
    while (notDone):
        notDone = False
        for [x,y] in pairs:
            if(s[y] < s[x]):
                temp1 = s[x]
                s[x] = s[y]
                s[y] = temp1
                notDone = True
    notDone = True
    pairs = pairs[::-1]
    while (notDone):
        notDone = False
        for [x,y] in pairs:
            if(sr[y] < sr[x]):
                temp1 = sr[x]
                sr[x] = sr[y]
                sr[y] = temp1
                notDone = True
    string1 = ""
    string2 = ""
    for a in s:
        string1 = string1 + str(a)
    for a in sr:
        string2 = string2 + str(a)
    print(string1)
    print(string2)
    return min(string1, string2)

print(smallestStringWithSwaps("dcab", [ [0,3], [1,2], [0,2]] ))