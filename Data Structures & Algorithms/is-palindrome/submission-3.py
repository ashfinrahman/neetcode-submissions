class Solution:
    def isPalindrome(self, s: str) -> bool:
        #turn string alphanum, reverse, check if same
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr += char
        #print(newstr[::-1].lower())
        return newstr[::-1].lower() == newstr.lower()
