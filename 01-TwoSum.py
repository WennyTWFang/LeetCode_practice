class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)< 2:
            #print("You must input length >= 2")
            return False
        elif len(nums)>10**4:
            #print("You must input the nums length < 10**4")
            return False
        elif type(nums) != list:
            return False
        if target< -10**9:
            return False
        elif target> 10**9:
            return False
        elif type(target) != int:
            return False
        #check each numbers
        for i in nums:
            if i >10 **9:
                return False
            elif i<-10**9:
                return False
        #Add number to other number
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                a = nums[i+1:]
                return [i, a.index(temp)+i+1]
