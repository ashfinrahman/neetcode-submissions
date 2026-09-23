class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for i in s:
            if i.isalnum():
                newstr += i.lower()

        for i in range(len(newstr)//2):
            if newstr[i] != newstr[-(i + 1)]:
                return False
        return True
        