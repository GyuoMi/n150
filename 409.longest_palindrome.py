import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)

        length = 0
        has_odd_center = False

        # add up all pairs
        for count in counts.values():
            # add even part of the count
            length += (count // 2) * 2
            # check if there is any character with an odd count
            if count % 2 == 1:
                has_odd_center = True

        if has_odd_center:
            length +=1

        return length
        
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         seen = set()
#         res = 0

#         for c in s:
#             if c in seen:
#                 seen.remove(c)
#                 res += 2
#             else:
#                 seen.add(c)

#         return res + 1 if seen else res

        