class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid = l + (r - l) // 2
            print(mid,l,r-l)
            if nums[mid] > target:
                r = mid -1
                print('r',r)
            elif nums[mid]<target:
                l = mid + 1
                print('l',l)
            else:
                return mid
        return -1
        