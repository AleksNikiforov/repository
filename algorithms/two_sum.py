class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        start_idx = 0
        for idx, num in enumerate(nums):
            for idx_2, num_2 in enumerate(nums):
                if num + num_2 == target and idx != idx_2:
                    solution = [idx, idx_2]
                    return solution
            start_idx += 1


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))