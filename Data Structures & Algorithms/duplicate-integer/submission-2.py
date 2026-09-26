class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #two method
        hashset = set()
        for i in nums:
            if i in hashset:
                return True 
            hashset.add(i)
        return False     
    
        #one method
    #    for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #    return False 

        

