class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums_set = set(nums)
        for item in nums:
            if item - 1 in nums_set:
                continue
            length = 0
            while item in nums_set:
                item += 1
                length += 1
            res= max(res, length)
        return res