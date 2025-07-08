# bucket sort linear time
# count: [0 1     2   3 4 5 6]
# value: [# [100] [2] [1]]
# we store the value as the index of how many times it is counted
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n) # n occurs c number of times

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n) # getting n that occurs most frequently
                if len(res) == k:
                    return res
# Time & Space Complexity
#
#     Time complexity: O(n)
#     Space complexity: O(n)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # count how many times the number appears in the input
        count = {}
        for num in nums:
                retrieves count and increments if seen, else just uses 0 
            count[num] = 1 + count.get(num, 0)
        # build min heap
        heap = []
        for num in count.keys():
            # each number a tuple is pushed onto the min-heap
            # smallest item on top
            # smallest frequency is on top since that is the first element in the tuple
            heapq.heappush(heap, (count[num], num))
            # if the heap size exceeds k remove the tuple with the lowest freq (pop off top)
            if len(heap) > k:
                heapq.heappop(heap)
        # the heap should now only contain the k most freq
        res = []
        for i in range(k):
            # 1 here accesses the number since we dont need to show the freq
            res.append(heapq.heappop(heap)[1])
        return res
"""
# Time & Space Complexity
#
#     Time complexity: O(nlogk)
#     Space complexity: O(n+k)

