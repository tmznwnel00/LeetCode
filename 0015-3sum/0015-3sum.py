class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            ret = []
            for i in range(len(nums)):
                l = 0
                r = i-1
                while l < r:
                    s = nums[l] + nums[r] + nums[i]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        tp = [nums[l], nums[r], nums[i]]
                        if tp not in ret:
                            ret.append(tp)
                        l += 1
                        # while l < r and nums[l] == tp[0]:
                        #     l += 1
                        # while r > l and nums[r] == tp[1]:
                        #     r -= 1
            return ret