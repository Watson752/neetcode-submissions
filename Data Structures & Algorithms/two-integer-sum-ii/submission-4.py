class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(numbers)<2:
            return -1
        
        index = [0,len(numbers)-1]

        for i in range(len(numbers)):
            if numbers[index[0]]+numbers[index[1]]==target:
                index[0]+=1
                index[1]+=1
                return index
            elif numbers[index[0]]+numbers[index[1]]<target:
                index[0]+=1
            else:
                index[1]-=1