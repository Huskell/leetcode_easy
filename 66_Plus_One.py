from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []
        number = ''
        for i in digits:
            number += str(i)

        number = int(number) + 1
        number = str(number)
        for i in number:
            result.append(i)
        return result


if __name__ == '__main__':
    input = [1, 2, 3, 9]

    print(Solution().plusOne(input))