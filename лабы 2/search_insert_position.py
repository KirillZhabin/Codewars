class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while (begin <= end):
            mid = (begin + end) // 2
            mid_val = nums[mid]

            if mid_val < target:
                begin = mid + 1
            elif mid_val > target:
                end = mid - 1
            else:
                return mid

        return begin