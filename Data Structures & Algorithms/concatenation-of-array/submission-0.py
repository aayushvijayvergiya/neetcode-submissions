class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

nums = [1,4,1,2]
sol = Solution()
print(sol.getConcatenation(nums))