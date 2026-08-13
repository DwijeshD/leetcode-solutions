
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))

            if key in keys:
                keys[key].append(word)
            else:
                keys[key] = [word]

        return list(keys.values())