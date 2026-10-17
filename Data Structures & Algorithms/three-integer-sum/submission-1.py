class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
       
        for i,j in enumerate(nums):

            if i>0 and j==nums[i-1]:#where it was duplicate pass it this iterate loop the sorted loop
                continue
            
            #how two pointer work algorithm
            l,r=i+1,len(nums)-1 #l mean left first value, r mean right last value
            while l<r:
                three_sum = j+nums[l]+nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([j,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and  l<r:#while the next left is same with previous left skip it
                        l+=1
        return ans