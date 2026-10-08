from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a table that tracks the counts of every words, charachters and have ord count it up, then from there make it a tuple and add it to the table.
        anagram_tab = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            anagram_tab[key].append(s)
        return list(anagram_tab.values())

        