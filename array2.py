class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(0,len(nums)):
            if(nums[i]==0):
                temp=nums[i]
                nums.remove(nums[i])
                nums.append(temp)
        return nums        
               

        
       
