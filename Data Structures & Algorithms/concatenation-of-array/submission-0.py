class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        nCounter = 0
        i = 0
        max_len = 2 * len(nums)

        while i < max_len:
            if i >= max_len/2:
                ans.append(nums[i - (int(max_len/2))])
            else:
                ans.append(nums[i])
            i = i + 1
        return ans