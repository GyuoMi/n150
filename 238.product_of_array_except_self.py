class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n 
        
        prefix = 1
        # compute nums from beginning to "i"
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # now we start at the end and go until the end
        postfix = 1
        for i in range(n - 1, -1, -1):
            # need to multiply otherwise just writing would overwrite
            res[i] *= postfix
            postfix *= nums[i]
        return res
