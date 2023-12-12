class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for i in range(len(nums))]
        postfix = [0 for i in range(len(nums))]

        for i in range(0, len(nums)):
            if i == 0:
                prefix[0] = nums[0]
            else:
                prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]

        solution = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                solution[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                solution[i] = prefix[i - 1]
            else:
                solution[i] = postfix[i + 1] * prefix[i - 1]
        
        return solution
