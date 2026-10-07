class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode the strs to have a # and the number of ch in that word
        encoded = []
        for i in strs:
            num = len(i)
            word = str(num) + "#" + i
            encoded.append(word)
        return "".join(encoded)

    #5hello#5world
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

