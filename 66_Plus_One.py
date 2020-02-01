from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = ''
        for i in digits:
            number += str(i)
        number = [ int(x) for x in str(int(number) + 1)]

        return number


if __name__ == '__main__':
    input = [1, 2, 3, 9]

    print(Solution().plusOne(input))