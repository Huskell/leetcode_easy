from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        valid = 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[valid] = nums[i]
                valid += 1
        return valid


if __name__ == '__main__':
    nums = [1,1,2]
    sol = Solution().removeDuplicates(nums)
    print(sol)