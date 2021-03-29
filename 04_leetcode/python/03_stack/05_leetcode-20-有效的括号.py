class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        flag = True
        for i in s:
            if i in ['(', '[', '{']:
                st.append(i)
            elif i == '}':
                flag = not (len(st)==0 or st.pop() != '{')
                if not flag:
                    return False
            elif i == ']':
                flag = not (len(st)==0 or st.pop() != '[')
                if not flag:
                    return False
            elif i == ')':
                flag = not (len(st)==0 or st.pop() != '(')
                if not flag:
                    return False
        return flag and len(st)==0

        # if len(s) % 2 != 0: return False
        # stack = []
        # dic = {')': '(', ']': '[', '}': '{'}
        # for s_i in s:
        #     if stack and s_i in dic and stack[-1] == dic[s_i]:
        #         stack.pop()
        #     elif s_i not in dic:
        #         stack.append(s_i)
        #     else:
        #         return False
        # return len(stack) == 0
