class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # make sure to set left pointer as 1 otherwise, div by zero error
        # also since we cant eat no bananas, need to eat at least 1 in that list of k
        # list of k [1, 2, 3 ... ,max(piles)]
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
        
            if total_time <= h:
                res = min(res, k)
                r = k - 1
            elif total_time > h:
                l = k + 1
            else: 
                return res
        return res
