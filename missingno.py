# missing no
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        b=sum(range(0,len(nums)+1))
        return b-a
        # a=nums.sort()
        # for i,x in enumerate(nums):
        #     if i!=x:
        #         return i
        # return len(nums)  

            

    
