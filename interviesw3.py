#Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        count=0
        ll=[]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                store=nums[i:j+1]
                min_store=min(store)
                max_store=max(store)
                if(max_store-min_store<=limit):
                    ll.append(len(store))
                    count=count+1
        return max(ll)            




import heapq

def longestSubarray(nums, limit):
    max_heap = []  # Max heap to store the maximum elements in the window
    min_heap = []  # Min heap to store the minimum elements in the window
    left = 0       # Left pointer of the window
    max_length = 0  # Length of the longest subarray

    for right in range(len(nums)):
        # Add the current element to the max and min heaps
        heapq.heappush(max_heap, -nums[right])  # Use negative values for max heap
        heapq.heappush(min_heap, nums[right])

        # Check if the absolute difference between the maximum and minimum elements in the window
        # is greater than the limit
        while -max_heap[0] - min_heap[0] > limit:
            # Remove elements from the left of the window until the condition is satisfied
            if nums[left] == -max_heap[0]:
                heapq.heappop(max_heap)
            if nums[left] == min_heap[0]:
                heapq.heappop(min_heap)
            left += 1

        # Update the maximum subarray length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
print(longestSubarray(nums, limit))  # Output: 2
