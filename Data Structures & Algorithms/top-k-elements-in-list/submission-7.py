# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         dic_map = {}

#         for i in nums: #count the number of times
#             dic_map[i] = 1 + dic_map.get(i,0)
           

#         arr = []

#         for i,j in dic_map.items(): #assign to new array and sorted that array 
#             arr.append([i,j])       # for find the value 
#         arr.sort()

#         ans = []

#         while len(ans)<k:  #find the k frequent elements with backward 
#             ans.append(arr.pop()[0])
#         return ans 




#  # if i in dic_map:
#             #      dic_map[i] += 1
#             # else:
#             #     dic_map[i] = 1
# # for i in dic_map:
#         #     if dic_map[i] >= k:
#         #         ans.append(i)
#         #     else:
#         #         continue
#         # if len(ans) == 0:
#         #     return nums
            
#         # return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
