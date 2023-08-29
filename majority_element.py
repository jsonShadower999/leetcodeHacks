lass Solution:
    def majorityElement(self, nums: List[int]) -> int:
        criticalpoint=len(nums)//2
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]=dict1[i]+1
        for k,v in dict1.items():
            if(dict1[k]>criticalpoint):
                return k
             
