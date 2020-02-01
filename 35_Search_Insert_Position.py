from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        s = 0
        e = len(nums) - 1

        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        while s <= e:
            q = (s + e) // 2
            if nums[q] == target:
                return q
            if (nums[q] > target and nums[q - 1] < target):
                return q
            if (nums[q + 1] > target and nums[q] < target):
                return q + 1

            if nums[q] > target:
                e = q - 1

            if nums[q] < target:
                s = q + 1

    def searchInsert2(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])

if __name__ == '__main__':
    nums = [1,3,5,6]
    val = 5
    print(Solution().searchInsert2(nums, val))