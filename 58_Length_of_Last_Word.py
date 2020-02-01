class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split()
        if len(st) == 0:
            return 0
        return len(st[-1])


if __name__ == '__main__':
    s = 'Hello World'
    s2 = '         '
    print(Solution.lengthOfLastWord(s))