class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify_down(nums, index):
            l = 2 * index + 1
            r = 2 * index + 2
            max_val = index
 
            length = len(nums) - 1
            if l <= length and nums[l] > nums[index]:
                max_val = l
            if r <= length and nums[r] > nums[index] and nums[r] > nums[l]:
                max_val = r

            if max_val != index:
                nums[index], nums[max_val] = nums[max_val], nums[index]
                heapify_down(nums, max_val)
                
        def heapify_up(nums, index):
            l = (index - 1) // 2
            max_val = index
   
            length = len(nums) - 1
            if l >= 0 and nums[l] < nums[index]:
                max_val = l
            if max_val != index:
                nums[index], nums[max_val] = nums[max_val], nums[index]
                heapify_up(nums, max_val)
        
        h = []
        for index, num in enumerate(nums):
            h.append(num)
            heapify_up(h, index)
        answer = 0
        

        
    
        for i in range(k):
            answer = h[0]
            # if answer != max(nums):
            #     print(answer, max(nums))
            # nums.remove(max(nums))
            h[0], h[-1] = h[-1], h[0]
            h.pop()

            heapify_down(h,0)
       
        return answer