class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        o = {}

        for i in range(len(nums)):
            if nums[i] not in o:
                o[nums[i]] = 1
            else:
                o[nums[i]] += 1
        
        ans_tup = sorted(o.items(), key = lambda item: item[1], reverse = True)

        ans = []
        for i in range(k):
            ans.append(ans_tup[i][0])
        
        print(ans)
        return ans