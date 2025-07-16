class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       numSet = set(nums) 
       longest = 0

       # numSet instead of nums since numSet will contain uniques, 
       # nums will check the same number multiple times leading to a time limit exceeded
       for n in numSet:
           # check if it's the start of a sequence
           if (n - 1) not in numSet: # if there is no left neighbour it is the start of a sequence
               # can be changed to 1 since 0 means the first check we do is redundant since
               # the starting loop is then just used to count the first number 
               length = 1
               while (n + length) in numSet:
                   length += 1
               longest = max(length, longest)
       return longest 
