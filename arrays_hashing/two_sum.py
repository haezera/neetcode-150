class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        index = 0
        for i in nums:
            if target - i in hash_map:
                return [hash_map[target - i], index]
            else:
                hash_map[i] = index
            index += 1
