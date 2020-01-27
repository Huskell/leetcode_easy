class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        num = len(s)
        if num % 2 != 0:
            s = s[:num//2] + s[num//2 + 1:]

        s1 = s[:num//2]
        s2 = s[num//2:]
        s2 = s2[::-1]

        flag = True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                flag = False
        return flag

if __name__ == '__main__':
    sol = Solution().isPalindrome(131)
    print(sol)