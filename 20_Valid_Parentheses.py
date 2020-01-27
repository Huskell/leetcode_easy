class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0: return False

        openP = ['(', '[', '{']
        closeP = [')', ']', '}']
        stack_list = str()
        print(stack_list)
        flag = True
        for i in range(len(s)):
            if s[i] in openP:
                stack_list += s[i]
            elif (s[i] in closeP) and (stack_list != ''):
                if (stack_list[-1] == openP[0] and s[i] == ')') or (stack_list[-1] == openP[1] and s[i] == ']') or (stack_list[-1] == openP[2] and s[i] == '}'):
                    stack_list = stack_list[:-1]
                else:
                    return False
            else:
                return False
        if stack_list == str():
            return flag
        else:
            return False

    def isValid_2(self, s: str) -> bool:
        pass


if __name__ == '__main__':
    p = '){'
    sol = Solution().isValid(p)
    print(sol)