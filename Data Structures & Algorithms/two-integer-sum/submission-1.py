class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}
        for index, item in enumerate(nums):
            diff = target - item
            if item in seen:
                result = [seen[item], index]
                break
            else:
                seen[diff] = index

        return result