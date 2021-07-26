class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)<1 or len(nums)>10**4:
            return False
        for i in nums:
            if i >10**4 or i<-10**4:
                return
        if target > 10**4 or target< -10**4:
            return False
        elif target == 0:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        close_low = 0#position
        close_high = len(nums)-1
        while close_low < close_high:
            middle = (close_low + close_high)//2
            if target > nums[middle]:
                close_low = middle
            elif target < nums[middle]:
                close_high = middle
            else:
                return middle
            if (close_low + 1) == close_high:
                return close_high
