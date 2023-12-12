    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_res = []
        nums.sort()
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    if sorted([nums[i], nums[l], nums[r]]) not in sorted_res:
                        res.append([nums[i], nums[l], nums[r]])
                        sorted_res.append(sorted([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
        return res
