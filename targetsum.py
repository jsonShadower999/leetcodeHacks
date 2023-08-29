class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        start=0
        summer=0
        def func(start,sumnow):
            if(start==len(nums)):
                return sumnow==target
            return func(start+1,sumnow+nums[start])+func(start+1,sumnow-nums[start])

        return func(start,summer)
    # def func(self,start,sumnow):
    #     if(start==len(nums)):
    #         return sumnow==target
    #     return self.func(start+1,sumnow+nums[start])+func(start+1,sumnow-nums[start])

      
