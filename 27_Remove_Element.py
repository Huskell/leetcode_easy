from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        for i in range(c):
            nums.remove(val)

        return len(nums)

    def removeElement2(self, nums, val):
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

if __name__ == '__main__':
    s = [1,2,2,4,5]
    val = 2
    print(Solution().removeElement(s, val))