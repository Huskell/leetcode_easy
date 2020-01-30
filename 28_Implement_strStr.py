class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == '': return 0
        n = len(needle)
        for i in range(n, len(haystack)+1):
            if needle == haystack[i-n:i]:
                return i-n

        return -1

if __name__ == '__main__':

    haystack = 'mississippi'
    needle = 'pi'
    sol = Solution().strStr(haystack, needle)
    print(sol)

    """string имеют метод find(), который возвращает индекс начала найденного отрезка"""