class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       indices = {}
       for i, n in enumerate(nums):
           indices[n] = i 
       for i, n in enumerate(nums):
           diff = target - n
           if diff in indices and indices[diff] != i:
               return [i, indices[diff]]
# Time & Space Complexity
#
#     Time complexity: O(n)
#     Space complexity: O(n)

    
