class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items_map = {}
        for item in nums:
            if item in items_map:
                return True
            else:
                items_map[item] = 1

        return False

    
nums = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDuplicate(nums))