from typing import List

#Для решения задачи используется алгоритм Кадане о поиске подмассива с наибольшей суммой
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best_sum = max(nums)
        current_sum = 0

        for x in nums:
            current_sum += x
            best_sum = max(best_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return best_sum


if __name__ == '__main__':
    Input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    'Output = 6'
    print(Solution().maxSubArray(Input))