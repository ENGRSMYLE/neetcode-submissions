class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # v -> i

        for i , v in enumerate(nums):
            diff = target - v 
            if diff in seen:
                return [seen[diff], i]

            seen[v] = i
        return []