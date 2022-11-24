class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        begin = 0
        end = len(arr) - 1

        while begin <= end:
            mid = (begin + end) // 2
            print(mid)
            
            if arr[mid - 1] > arr[mid]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                begin = mid
            else:
                return mid