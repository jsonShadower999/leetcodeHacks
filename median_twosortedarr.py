class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr_final=[]
        a1=0
        a2=0
        while(a1<len(nums1) and a2<len(nums2)):
            if(nums1[a1]<=nums2[a2]):
                arr_final.append(nums1[a1])
                a1=a1+1
            elif(nums1[a1]>nums2[a2]):
                arr_final.append(nums2[a2])
                a2=a2+1
        while( a2<len(nums2)):
            arr_final.append(nums2[a2])
            a2=a2+1
              
        while(a1<len(nums1)):
            arr_final.append(nums1[a1]) 
            a1=a1+1
        final_len=len(arr_final)  
        mid=final_len//2       
        if(len(arr_final)%2==0):
            return (arr_final[mid]+arr_final[mid-1])/2
        else:
            return arr_final[mid]    
          
