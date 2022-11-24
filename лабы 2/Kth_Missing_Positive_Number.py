class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = 0
        left = 0
        right = len(arr) 
        while left < right:
          mid = left + (right - left) // 2
          if arr[mid] - (mid + 1) >= k:
            right = mid
          else:
            left = mid + 1
        res = left + k
        return res