class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=len(ratings)
        left,right=[1]*l,[1]*l
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            
        for i in range(l-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
            
        for i in range(l):
            left[i]=max(left[i],right[i])
        return sum(left)
