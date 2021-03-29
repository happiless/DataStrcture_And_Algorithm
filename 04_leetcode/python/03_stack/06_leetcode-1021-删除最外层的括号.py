class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        pre = 0
        cnt = 0
        ret = []
        for i in range(len(S)):
            if S[i] == '(': cnt += 1
            else: cnt -= 1
            if cnt !=0: continue
            ret.append(S[pre + 1:i])
            pre = i + 1
        return ''.join(ret)