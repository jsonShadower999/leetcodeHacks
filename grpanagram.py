class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper={}
        for s in strs:
            sorted_str=''.join(sorted(s))
            if sorted_str not in mapper:
                mapper[sorted_str]=[]
            mapper[sorted_str].append(s)   
        return list(mapper.values())     
    #     i=0
    #     list_final=[]
    #     for j in range(0,len(strs)):
    #         list1=[]
    #         list1.append(list1[i])
    #         obj1=self.inner(strs[i])
    #         obj2=self.inner(strs[j])
    #         if(obj1==obj2):
    #             list1.append(strs[j])
    #             list_final.append(list1)
    #         else:
    #             list2=[]
    #             list2.append(strs[j])
    #             list_final.append(list2)
    #     i=i+1
    #     return list_final     
    # def inner(self,str1):
    #     dict1={}
    #     for i in str1:
    #         if i not in dict1:
    #             dict1[i]=1
    #         else:
    #             dict1[i]=dict1[i]+1
    #     return dict1
 






       
