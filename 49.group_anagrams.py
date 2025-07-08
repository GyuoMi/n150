class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            # python keys are immutable (cant be changed)
            # count is mutable so we cant use it as a key
            res[tuple(count)].append(s) 
        return list(res.values())


# Time complexity: O(m∗n)
# Space complexity:
#     O(m) extra space.
#     O(m∗n) space for the output list.



# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         map = defaultdict(list)
#
#         for word in strs:
#             key = ''.join(sorted(word))
#             map[key].append(word)
#
#         return [map[i] for i in map.keys() ]
