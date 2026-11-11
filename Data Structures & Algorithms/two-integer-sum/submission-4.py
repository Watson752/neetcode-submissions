class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        
        for i in range(len(nums)):
            d.update({nums[i]:i})
        
        
        for i in range(len(nums)):
            difference = target - nums[i]
            print(difference)
            if d.get(difference) != None and d.get(difference) != i:
                return [i,d[difference]]
        



