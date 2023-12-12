class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set()
        n = len(nums)
        for i in range(0, n):
            if nums[i] in setNums:
                return True
            else:
                setNums.add(nums[i])

        return False
