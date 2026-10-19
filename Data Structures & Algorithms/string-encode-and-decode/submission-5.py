class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            new = ""
            leng = str(len(word))
            new += leng + "#" + word
            res.append(new)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            leng = int(s[i:j])
            i = j + 1
            j = i + leng
            res.append(s[i:j])
            i = j
        return res 
