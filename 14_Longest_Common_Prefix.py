from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ""

        prefix = strs[0]

        if len(strs) == 1:
            return prefix

        for i in strs[1:]:
            prefix = prefix[:min(len(prefix), len(i))]
            for j in range(len(prefix)):
                if prefix[j] != i[j]:
                    prefix = prefix[:j]
                    break
        return prefix

if __name__ == '__main__':
    sol = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(sol)
