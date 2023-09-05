//remove duplicate n return new array len
class Solution {
    public int removeDuplicates(int[] nums) {
       int j=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=nums[i-1]){ // duplicate why prev==curr
                nums[j]=nums[i]; // override the duplicate element
                j++; // my next unique ele pointer
                
            }
        }
        return j;
    }
}
        // # s=set(nums)
        // # nums.clear()
        // # for i in s:
        // #     nums.append(i)
        // # nums.sort()
        // # return len(nums)    
