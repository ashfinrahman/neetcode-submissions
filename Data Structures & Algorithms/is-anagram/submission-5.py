class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        for i in s:
            if i not in sdict:
                sdict[i] = 1
            else:
                sdict[i] += 1
        tdict = {}
        for i in t:
            if i not in tdict:
                tdict[i] = 1
            else:
                tdict[i] += 1

        return tdict == sdict
        