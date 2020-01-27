class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0

        sol = str(x)

        if x >= 0:
            sign = str()
        else:
            sign = sol[0]
            sol = sol[1:]

        sol = sol[::-1]

        if int(sol) >= 2 ** 31 - 1 or int(sol) <= -2 ** 31: return 0

        return int(sign + sol)

if __name__ == "__main__":

    s = Solution()
    print(0xffffffff)
    print(s.reverse(1534236469))