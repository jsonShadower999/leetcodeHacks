
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=0
        last_p=0
        window=0
        for i in range(len(nums)):
            if(nums[i]==target):
                return 1
            window=window+nums[i]
            if(window<target):
                pass
            else:
                while window>=target:
                    temp=i-last_p+1
                    res=min(res,temp) if res!=0 else temp
                    window=window-nums[last_p]
                    last_p+=1
        return res                    
       
        # start=0
        # ans=1000
        # end=start
        # while(end<len(nums)):
        #     summer=nums[start:end]
        #     if(sum(summer)<target):
        #         end=end+1
        #     elif(sum(summer)==target):
        #         ans=min(ans,len(summer))
        #         end=end+1
        #     else:
        #         start=start+1
              
        # return ans             
