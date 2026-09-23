class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for i in strs:
            encodedstr += "^^"
            encodedstr += i
            encodedstr+= "||"
        print(encodedstr)
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedstr = []
        addstr = ""
        i = 0
        while i < len(s):
            if s[i] == '^' and s[i+1] == '^':
                addstr = ""
                print(addstr)
                i += 2
            elif s[i] == '|' and s[i+1] == '|':
                decodedstr.append(addstr)
                print(addstr)
                i += 2
            else:
                addstr += s[i]
                print(addstr)
                i += 1
        return decodedstr

