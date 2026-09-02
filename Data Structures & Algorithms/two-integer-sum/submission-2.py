from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)

        hashmap = defaultdict(list)
        output_pair = []

        for i in range(nums_len):
            hashmap[nums[i]].append(i)

        # for i in range(nums_len):
        #     # hashmap[nums[i]] = i

        #     if ((target - nums[i]) in hashmap) and (hashmap[(target - nums[i])] != i):
        #         output_pair.append(i)

        for i in range(nums_len):
            if len(hashmap[nums[i]]) == 1:
                hashmap.pop(nums[i], None)

            if ((target - nums[i]) in hashmap):
                output_pair.append(i)

            hashmap[nums[i]].append(i)
        
        output_pair.sort()

        return output_pair


        
