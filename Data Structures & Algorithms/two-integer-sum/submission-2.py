class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        for i in range(len(nums)):
            sums.append(target - nums[i])
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == sums[j]:
                    return[i,j]
