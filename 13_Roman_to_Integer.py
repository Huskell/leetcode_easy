class Solution:
    def romanToInt(self, s: str) -> int:
        dictRoman = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}

        listRoman = []
        summ = 0
        for i in s:
            listRoman.append(dictRoman[i])

        while listRoman:
            summ += max(listRoman)
            if listRoman.index(max(listRoman)) == 0:
                listRoman.remove(max(listRoman))
            else:
                listRomanShort = listRoman[:listRoman.index(max(listRoman))]
                for i in reversed(listRomanShort):
                    summ -= i
                listRoman = listRoman[listRoman.index(max(listRoman))+1:]

        return summ






if __name__ == '__main__':
    sol = Solution().romanToInt("IX")
    print(sol)
    sol = Solution().romanToInt("MCMXCIV")
    print(sol)