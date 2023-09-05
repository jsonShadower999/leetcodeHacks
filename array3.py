#product of array except self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lp=[1]*n
        rp=[1]*n
        pproduct=1
        for i in range(n):
            lp[i]=pproduct
            pproduct=pproduct*nums[i]
        sproduct=1
        for i in range(n-1,-1,-1):
            rp[i]=sproduct
            sproduct=sproduct*nums[i]
        res=[lp[i]*rp[i] for i in range(n)]
        return res
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     def mul(arr):
    #         res=1
    #         for i in range(len(arr)):
    #             res=res*arr[i]
    #         return res    
    #     l=[]
    #     for i in range(0,len(nums)):
    #        a= mul(nums[:i]) 
    #        b=mul(nums[i+1:])
    #        c=a*b
    #        l.append(c)
    #     return l


       

        
